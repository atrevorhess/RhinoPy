import rhinoscriptsyntax as rs
from Object import Object
import CurveTools

class LineObject(Object):
    def __init__(self, guid):
        Object.__init__(self, guid)

    def __get__(self, instance, owner):
        return self.GUID

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass

    def __len__(self): #length
        return CurveTools.length(self.GUID)

    def _isLine(self, rhino_object):
        return rs.IsLine(rhino_object.GUID)
        
    def angle(self, line):
        return rs.Angle2(self.GUID, line.GUID)

    def closestPoint(self, test_point):
        return rs.LineClosestPoint(self.GUID, test_point.GUID)

    def copy(self, translation=None):
        #What code is needed for the copy Object method to return a line
        return Line(rs.CopyObject(self.GUID, translation))

    def isFartherThan(self, distance, point_or_line):
        return rs.LineIsFartherThan(self.GUID, distance, point_or_line.GUID)

    def intersect(self, intersection_object):
        # if rs.IsCylinder(intersection_object):
        #     return rs.LineCylinderIntersection(self.GUID, intersection_object.GUID)
        if rs._isLine(intersection_object):
            return rs.LineLineIntersection(self.GUID, intersection_object.GUID)
        # if rs.IsPlaneSurface(intersection_object):
        #     return rs.LinePlaneIntersection(self.GUID, intersection_object.GUID)
        # if rs.IsSphere(intersection_object):
        #     return rs.LineSphereIntersection(self.GUID, intersection_object.GUID)

    def maxDistance(self, point_or_line):
        return rs.LineMaxDistanceTo(self.GUID, point_or_line.GUID)

    def minDistance(self, point_or_line):
        return rs.LineMinDistanceTo(self.GUID, point_or_line.GUID)

    def plane(self):
        return rs.LinePlane(self.GUID)

    def transform(self, xform):
        return rs.LineTransform(self.GUID, xform)

class Line(LineObject):
    def __init__(self, points):
        LineObject.__init__(self, self._add(points))

    def _add(self, points):
        return rs.AddLine(points[0], points[1])

class Polyline(LineObject):
    def __init__(self, points, replace_id=None):
        LineObject.__init__(self, self._add(points, replace_id))

    def _add(self, points, replace_id=None):
        return rs.AddPolyline(points, replace_id)

if __name__ == '__main__':
    line = Line([[0, 0, 0], [2, 2, 2]])
    line2 = Line([0, 0, 0], [-2, -2, 2])
    line.color([255, 255, 255])
    line3 = line.copy([0, 0, 2])
    line.intersect(line2)
    line.maxDistance(line2)
    line.minDistance(line2)
    line.plane()
