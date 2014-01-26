import rhinoscriptsyntax as rs
# import Object

class Plane:
    def __init__(self):
        self.GUID
        """
        Constructors
        PlaneFitFromPoints()
        PlaneFromFrame
        PlaneFromNormal(self)
        PlaneFromPoints()
        """
        pass

def DistanceToPlane(self, point):
    return rs.DistanceToPlane(self.GUID, point)

def EvaluatePlane(self, parameter):
    return rs.EvaluatePlane(self.GUID, parameter)

def IntersectPlanes(self, plane2, plane3):
    return rs.IntersectPlanes(self.GUID)

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
    
def PlaneTransform(self, xform):
    return rs.PlaneTransorm(self.GUID, xform)

def RotatePlane(self, angle_degrees, axis):
    return rs.RotatePlane(self.GUID, angle_degrees, axis)

def WorldXYPlane(self):
    pass

def WorldYZPlane(self):
    pass

def WorldZXPlane(self):
    pass