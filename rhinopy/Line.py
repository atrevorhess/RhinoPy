import rhinoscriptsyntax as rs
from Object import Object

class Line(Object):
    def __init__(self, points, hidden=False, locked=False, selected=False):
        self.GUID = self._add(points)

    def _add(self, points):
        return rs.AddLine(points[0], points[1])
        
    def angle(self, line):
        return rs.Angle2(self.GUID, line.GUID)

    def closestPoint(self, test_point):
        return rs.LineClosestPoint(self.GUID, test_point.GUID)

    def isFartherThan(self, distance, point_or_line):
        return rs.LineIsFartherThan(self.GUID, distance, point_or_line.GUID)

    def intersect(self, intersection_object):
        if rs.IsCylinder(intersection_object):
            return rs.LineCylinderIntersection(self.GUID, intersection_object.GUID)
        if rs.IsLine(intersection_object):
            return rs.LineLineIntersection(self.GUID, intersection_object.GUID)
        if rs.IsPlaneSurface(intersection_object):
            return rs.LinePlaneIntersection(self.GUID, intersection_object.GUID)
        if rs.IsSphere(intersection_object):
            return rs.LineSphereIntersection(self.GUID, intersection_object.GUID)

    def maxDistance(self, point_or_line):
        return rs.LineMaxDistanceTo(self.GUID, point_or_line.GUID)

    def minDistance(self, point_or_line):
        return rs.LineMinDistanceTo(self.GUID, point_or_line.GUID)

    def plane(self):
        return rs.LinePlane(self.GUID)

    def transform(self, xform):
        return rs.LineTransform(self.GUID, xform)

if __name__ == '__main__':
    line = Line([[0, 0, 0], [2, 2, 2]])
    rs.DivideCurve(line, 3, True)