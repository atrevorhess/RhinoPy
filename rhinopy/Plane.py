import rhinoscriptsyntax as rs
from Object import Object

class PlaneObject(Object):
    def __init__(self, guid):
        Object.__init__(self, guid)
        
    def distanceToPlane(self, point):
        return rs.DistanceToPlane(self.GUID, point)

    def evaluate(self, parameter):
        return rs.EvaluatePlane(self.GUID, parameter)

    # def intersectPlanes(self, plane2, plane3):
    #     # Used for to intersect three planes
    #     return rs.IntersectPlanes(self.GUID)

    def move(self, origin):
        return rs.MovePlane(self.GUID, origin)

    def closestPoint(self, point, return_point=True):
        return rs.PlaneClosestPoint(self.GUID, point, return_point)

    def equation(self):
        return rs.PlaneEquation(self.GUID)

    def intersection(self, intersection_object):
        if rs.IsCurve(intersection_object):
            return rs.CurveIntersection(self.GUID, intersection_object)
        if rs.IsPlane(intersection_object):
            return rs.PlanePlaneIntersection(self.GUID, intersection_object)
        if rs.IsSphere(intersection_object):
            return rs.PlaneSphereIntersection(self.GUID, intersection_object)
        
    def transform(self, xform):
        return rs.PlaneTransorm(self.GUID, xform)

    def rotate(self, angle_degrees, axis):
        return rs.RotatePlane(self.GUID, angle_degrees, axis)

class PlaneFitFromPoints(PlaneObject):
    def __init__(self, points):
        PlaneObject.__init__(self, self._add(points))

    def _add(self, points):
        return rs.PlaneFitFromPoints(points)

class PlaneFromFrame(PlaneObject):
    def __init__(self, origin, x_axis, y_axis):
        PlaneObject.__init__(self, self._add(origin, x_axis, y_axis))

    def _add(self, origin, x_axis, y_axis):
        return rs.PlaneFromFrame(origin, x_axis, y_axis)

class PlaneFromNormal(PlaneObject):
    def __init__(self, origin, normal, x_axis=None):
        PlaneObject.__init__(self, self._add(origin, normal, x_axis))

    def _add(self, origin, normal, x_axis=None):
        return rs.PlaneFromNormal(origin, normal, x_axis)

class PlaneFromPoints(PlaneObject):
    def __init__(self, origin, x, y):
        PlaneObject.__init__(self, self._add(origin, x, y))

    def _add(self, origin, x, y):
        return rs.PlaneFromPoints(origin, x, y)

class WorldXYPlane(PlaneObject):
    def __init__(self):
        PlaneObject.__init__(self, self.self._add(self))

    def _add(self):
        return rs.WorldXYPlane()

class WorldYZPlane(PlaneObject):
    def __init__(self):
        PlaneObject.__init__(self, self._add(self))

    def _add(self):
        return rs.WorldYZPlane()

class WorldZXPlane(PlaneObject):
    def __init__(self):
        PlaneObject.__init__(self, self._add(self))

    def _add(self):
        return rs.WorldZXPlane()
