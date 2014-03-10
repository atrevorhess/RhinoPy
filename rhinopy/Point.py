import rhinoscriptsyntax as rs
from Object import Object

class PointObject(Object):
    def __init__(self, guid):
        Object.__init__(self, guid)

    def _isPoint(self, object):
        pass

    def angle(self, point, plane=True):
        return rs.Angle(self.GUID, point.GUID)

    def coordinates(self, point=None):
        return rs.PointCoordinates(self.GUID, point.GUID)

    def arrayClosestPoint(self):
        pass

    def closestObject(self, objects):
        return rs.PointClosestObject(self.GUID, objects.GUID)

    def compare(self, point, tolerance=None):
        return rs.PointCompare(self.GUID, point.GUID, tolerance)

    def copy(self, translation=None):
        return PointObject(rs.CopyObject(self.GUID, translation))

    def divide(self, divide):
        self.GUID = PointObject(rs.PointDivide(self.GUID, divide))

    def coplanar(self, points, tolerance = 1.0e-12):
        return rs.PointsAreCoplanar(points.append(self.GUID), tolerance)

    def mirror(self, start_point, end_point, copy=False):
        return Point(rs.MirrorObject(self.GUID, start_point.GUID, end_point.GUID, copy))

    def scale(self, scale):
        self.GUID = PointObject(rs.PointScale(self.GUID, scale))

    def transform(self, xform):
        self.GUID = rs.PointTranform(self.GUID, xform)

    def project(self, projection_object, direction):
        if rs.IsMesh(projection_object):
            return Point(rs.ProjectPointToMesh(self.GUID, projection_object, direction))
        if rs.IsSurface(projection_object):
            return Point(rs.ProjectPointToMesh(self.GUID, projection_object, direction))

class Point(PointObject):
    def __init__(self, coordinates):
        PointObject.__init__(self, self._add(coordinates))

    def _add(self, coordinates):
        return rs.AddPoint(coordinates)

class PolarPoint(PointObject):
    def __init__(self, origin, angle_degrees, distance, plane=None):
        Point.__init__(self, self._add(origin, angle_degrees, distance, plane))

    def _add(self, origin, angle_degrees, distance, plane=None):
        return rs.Polar(origin, angle_degrees, distance, plane)

if __name__ == '__main__':
    pt1 = Point([0, 0, 0])
    pt2 = pt1.copy([0, 2, 2])
    pt3 = pt2.copy([0, 0, -4])