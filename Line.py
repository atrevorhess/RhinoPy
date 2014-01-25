import rhinoscriptsyntax as rs
from Object import Object

class Line(Object):
    def __init__(self, points):
        self.GUID = self._draw(points)

    def __get__(self):
        return self.GUID
        
    def __getattr__(self):
        return self.GUID

    def __repr__(self):
        return self.GUID

    def __str__(self):
        return self.GUID

    def _draw(self, points):
        return rs.AddLine(points[0], points[1])
        
    def angle(self, line):
        return rs.Angle2(self.GUID, line)

    def closestPoint(self, test_point):
        return rs.LineClosestPoint(self.GUID, test_point)

    def isFartherThan(self, distance, point_or_line):
        return rs.LineIsFartherThan(self.GUID, distance, point_or_line)

    def intersection(self, intersection_object):
        if rs.IsCylinder(intersection_object):
            return rs.LineCylinderIntersection(self.GUID, intersection_object)
        if rs.IsLine(intersection_object):
            return rs.LineLineIntersection(self.GUID, intersection_object)
        if rs.IsPlaneSurface(intersection_object):
            return rs.LinePlaneIntersection(self.GUID, intersection_object)
        if rs.IsSphere(intersection_object):
            return rs.LineSphereIntersection(self.GUID, intersection_object)

    def maxDistance(self, point_or_line):
        return rs.LineMaxDistanceTo(self.GUID, point_or_line)

    def minDistance(self, point_or_line):
        return rs.LineMinDistanceTo(self.GUID, point_or_line)

    def plane(self):
        return rs.LinePlane(self.GUID)

    def transform(self, xform):
        return rs.LineTransform(self.GUID, xform)

if __name__ == '__main__':
    line = Line([[0, 0, 0], [2, 2, 2]])
    rs.DivideCurve(line, 3, True)