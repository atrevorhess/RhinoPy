import rhinoscriptsyntax as rs
from Object import Object

class Point(Object):
    def __init__(self, constructor, hidden=False, locked=False, selected=False):
        self.GUID = constructor if self._isPoint(constructor) else self._add(constructor)

    def __str__(self):
        return self.coordinates()

    def __repr__(self):
        return self.GUID

    def _draw(self, coordinate_list):
        return rs.AddPoint(coordinate_list)

    def _isPoint(self, object):
        pass

    def coordinates(self, point=None):
        return rs.PointCoordinates(self.GUID, point)

    def copy(self, translation=None):
        return Point(rs.CopyObject(self.GUID, translation))

    def arrayClosestPoint(self):
        pass

    def closestObject(self, objects):
        return rs.PointClosestObject(self.GUID, objects)

    def compare(self, point, tolerance=None):
        return rs.PointCompare(self.GUID, point, tolerance)

    def divide(self, divide):
        self.GUID = Point(rs.PointDivide(self.GUID, divide))

    def coplanar(self, points, tolerance = 1.0e-12):
        return rs.PointsAreCoplanar(points.append(self.GUID), tolerance)

    def mirror(self, start_point, end_point, copy=False):
        return Point(rs.MirrorObject(self.GUID, start_point, end_point, copy))

    def scale(self, scale):
        self.GUID = Point(rs.PointScale(self.GUID, scale))

    def transform(self, xform):
        self.GUID = rs.PointTranform(self.GUID, xform)

    def project(self, projection_object, direction):
        if rs.IsMesh(projection_object):
            return Point(rs.ProjectPointToMesh(self.GUID, projection_object, direction))
        if rs.IsSurface(projection_object):
            return Point(rs.ProjectPointToMesh(self.GUID, projection_object, direction))

if __name__ == '__main__':
    #Insert Testing Code Below
    
    pt1 = Point([0,0,0])
    pt2 = Point([2, 0, 0])

    pt1.copy([0,0,1])
    pt2.move([0,0,1])
    pt2.copy([0,0,1])