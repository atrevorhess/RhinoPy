import rhinoscriptsyntax as rs
from Object import Object
import CurveTools

class Line(Object):
    def __init__(self, points, hidden=False, locked=False, selected=False):
        self.GUID = self._add(points)

    def _add(self, points):
        return rs.AddLine(points[0], points[1])
    
    def _isLine(self, rhino_object):
        return rs.IsLine(rhino_object.GUID)

    def __get__(self, instance, owner):
        return self.GUID

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass

    def __add__(self, other): #Addition
        """
        if curve: Join Curve
        if number: extendLength
        """
        pass

    def __iadd__(self, other): #Addition with assignment
        """
        if curve: Join Curve
        if number: extendLength
        return new curve
        """
        pass

    def __sub__(self, other): #Subtraction
        pass

    def __isub__(self, other): #Subtraction with assignment
        pass

    def __mul__(self, other): #Multiplication
        pass

    def __imul__(self, other): #Multiplication with assignment
        pass

    def __div__(self, other): #Division
        """
        Divide Curve
        """
        pass

    def __idiv__(self, other): #Division with assignment
        pass

    def __len__(self): #length
        return CurveTools.length(self.GUID)

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