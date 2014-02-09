import rhinoscriptsyntax as rs
from Object import Object
from Plane import Plane
from Point import Point

class Curve(Object):
    def __init__(self, points, degree=3):
        self.GUID = rs.AddCurve(points, degree=degree, hidden=False, locked=False, selected=False)
        # Object.__init__(self, rs.AddCurve(points, degree=degree))
        #LineFitFromPoints Contructor

    def _isCurve(self, obj):
        return rs.IsCurve(obj)

    def fillet(self, curve_id, radius=1.0, base_point0=None, base_point1=None):
        #?? Returns GUID of new fillet, should the fillet be a seperate object ??
        return rs.AddFilletCurve(self.GUID, curve_id, radius=1.0, base_point0=None, base_point1=None)

    def arcLengthPoint(self, length, from_start=True):
        """
        Returns the point on the curve that is a specified arc length from the start of the curve.
        """
        return rs.CurveArcLengthPoint(self.GUID, length, from_start)

    def area(self):
        """
        Returns the area of self as a list specifying the area and absolute (+/-) error for the area
        [0] - Number - Area
        [1] - Number - +/- error
        """
        return rs.CurveArea(self.GUID)

    def areaCentroid(self):
        """
        Returns the area centroid of closed, planar curves.
        [0] - Point - Centroid
        [1] - (x,y,z) - +/- error
        """
        centroid, error = rs.CurveAreaCentroid(self.GUID)
        return Point(centroid), error

    def arrows(self, arrow_style=None):
        """
        Toggles a curve object's annotation arrows.
        If a style is specified the method returns the previous annotation style if successful. If a style is not specified the method returns the current annotation style.
        If not successful, or on an error, the method returns None
        """
        return rs.CurveArrows(self.GUID, arrow_style)

    def booleanDifference(self, curve):
        """
        Calculates the difference between self and another curve the results to the document.
        Curves must be coplanar.
        If successful the method returns a list of new objects
        If unsuccessful the method returns None
        """
        return rs.CurveBooleanDifference(self.GUID, curve)

    def booleanInteresection(self, curve):
        """
        Calculates the intersection between self and another curve the results to the document.
        Curves must be coplanar.
        If successful the method returns a list of new objects
        If unsuccessful the method returns None
        """
        return rs.CurveBooleanIntersection(self.GUID, curve)

    def booleanUnion(self, curve):
        """
        Calculates the union between self and another curve the results to the document.
        Curves must be coplanar.
        If successful the method returns a list of new objects
        If unsuccessful the method returns None
        """
        return rs.CurveBooleanUnion(self.GUID, curve)

    def brepInteresect(self, brep, tolerance=None):
        return rs.CurveBrepIntersect(self.GUID, brep, tolerance)

    def closestObject(self, objects):
        return rs.CurveClosestObject(self.GUID, objects)

    def closestPoint(self, test_point, segment_index=-1):
        return rs.CurveClosestPoint(self.GUID, test_point, segment_index)
    
    def contourPoints(self, start_point, end_point, interval=None):
        return rs.CurveContourPoints(self.GUID, start_point, end_point, interval)

    def curvature(self, parameter):
        return rs.CurveCurvature(self.GUID, parameter)

    def interesection(self, object):
        """
        Covers all the intersect functions. Test the object for type (brep, curve, surface, sphere, etc) then execute the corresponding intersection function
        Implement all intersection functions as internal psuedo private methods
        """
        pass

    def degree(self, segment_index=-1):
        """
        Returns the degree of the curvature of self
        """
        return rs.CurveDegree(self.GUID, segment_index)

    def deviation(self, curve):
        return rs.CurveDeviation(self.GUID, curve)

    def dim(self, segment_index=-1):
        return rs.CurveDim(self.GUID, segment_index)

    def directionsMatch(self, curve):
        return rs.CurveDirectionsMatch(self.GUID, curve)

    def discontinuity(self, style):
        return rs.CurveContinuity(self.GUID, style)

    def domain(self, segment_index=-1):
        return rs.CurveDomain(self.GUID, segment_index)

    def editPoints(self, return_parameters=False, segment_index=-1):
        return rs.CurveEditPoints(self.GUID, return_parameters, segment_index)

    def endPoints(self):
        #return start and end points
        return [Point(rs.CurveStartPoint(self.GUID)), Point(rs.CurveEndPoint(self.GUID))]

    def evaluate(self, parameter, index=-1):
        return rs.EvaluateCurve(self.GUID, parameter, index)

    def filletPoints(self, curve, radius=1.0, base_point_self=None, base_point_curve=None, return_points=True):
        return rs.CurveFilletPoints(self.GUID, curve, radius, base_point_self, base_point_curve, return_points)

    def frame(self, parameter, segment_index=-1):
        return rs.CurveFrame(self.GUID, parameter, segment_index)

    def knotCount(self, segment_index):
        return rs.CurveKnotCount(self.GUID, segment_index)

    def knots(self, segment_index=-1):
        return rs.CurveKnots(self.GUID, segment_index)

    def length(self, segment_index=-1, sub_domain=None):
        return rs.CurveLength(self.GUID, segment_index, sub_domain)

    def midpoint(self, segment_index=-1):
        return rs.CurveMidPoint(self.GUID, segment_index)

    def normal(self, segment_index=-1):
        return rs.CurveNormal(self.GUID, segment_index)

    def normalizedParameter(self, parameter):
        return rs.CurveNormalizedParameter(self.GUID, parameter)

    def parameter(self, parameter):
        return rs.CurveParameter(self.GUID, parameter)

    def perpFrame(self, parameter):
        return rs.CurvePerpFrame(self.GUID, parameter)

    def plane(self, segment_index=-1):
        return Plane(rs.CurvePlane(self.GUID, segment_index))

    def pointCount(self, segment_index):
        return rs.CurvePointCount(self.GUID, segment_index)

    def points(self, segment_index=-1):
        return rs.CurvePoints(self.GUID, segment_index)

    def radius(self, test_point, segment_index=-1):
        return rs.CurveRadius(self.GUID, test_point, segment_index)

    def seam(self, parameter):
        return rs.CurveSeam(self.GUID, parameter)

    def tangent(self, parameter, segment_index=-1):
        return rs.CurveTangent(self.GUID, parameter, segment_index)

    def weights(self, segment_index=-1):
        return rs.CurveWeights(self.GUID, segment_index)

    def divide(self, segments, create_points=False, return_points=True):
        return rs.DivideCurve(self.GUID, segments, create_points, return_points)

    def divideEquidistant(self, distance, create_points=False, return_points=True):
        return rs.DivideCurveEquidistant(self.GUID, distance, create_points, return_points)

    def divideLength(self, length, create_points=False, return_points=True):
        return rs.DivideCurveLength(self.GUID, length, create_points, return_points=True)

    def explode(self):
        # Method of Polylines or polycurves
        pass

    def extend(self, extension_type, side, boundary_object_ids):
        return rs.ExtendCurve(self.GUID, extension_type, side, boundary_object_ids)

    def extendLength(self, extension_type, side, length):
        return rs.ExtendCurveLength(self.GUID, extension_type, side, length)

    def extendToPoint(self, side, point):
        return rs.ExtendCurvePoint(self.GUID, side, point)

    def fair(self, tolerance=1.0):
        rs.FairCurve(self.GUID, tolerance)

    def fit(self, degree=3, distance_tolerance=-1, angle_tolerance=-1):
        return rs.FitCurve(self.GUID, degree, distance_tolerance, angle_tolerance)

    def insertKnot(self, parameter, symetrical=False):
        return rs.InsertCurveKnot(self.GUID, parameter, symetrical)

    def isClosable(self, tolerance=None):
        return rs.IsCurveClosable(self.GUID, tolerance)

    def isClosed(self):
        return rs.IsCurveClosed(self.GUID)

    def isInPlane(self, plane=None):
        return rs.IsCurveInPlane(self.GUID, plane)

    def isLinear(self, segment_index=-1):
        return rs.IsCurveLinear(self.GUID, segment_index)

    def isPeriodic(self, segment_index=-1):
        return rs.IsCurvePeriodic(self.GUID, segment_index)

    def isPlanar(self, segment_index):
        return rs.IsCurvePlanar(self.GUID, segment_index)

    def isPointOnCurve(self, point, segment_index=-1):
        return rs.IsPointOnCurve(self.GUID, point, segment_index=-1)

    def isPolyCurve(self, segment_index=-1):
        return rs.IsPolyCurve(self.GUID, segment_index)

    def isPolyline(self, segment_index=-1):
        return rs.IsPolyline(self.GUID, segment_index=-1)

    def isRational(self, segment_index=-1):
        return rs.IsCurveRational(self.GUID, segment_index)

    def join(self, curves, delete_input=False, tolerance=None):
        return rs.JoinCurves(curves.append(self.GUID), delete_input, tolerance)

    def makeNonPeriodic(self, delete_input=False):
        return rs.MakeCurveNonPeriodic(self.GUID, delete_input)

    def makePeriodic(self):
        pass

    def mean(self, curve, tolerance=None):
        return rs.MeanCurve(self.GUID, curve, tolerance)

    def meshPolyline(self):
        return rs.MeshPolyline(self.GUID)

    def offset(self, direction, distance, normal=None, style=1):
        return rs.OffsetCurve(self.GUID, direction, distance, normal, style)

    def offsetOnSurface(self, surface, distance_or_parameter):
        return rs.OffsetCurveOnSurface(self.GUID, surface, distance_or_parameter)

    def planarClosedContainment(self, curve, plane=None, tolerance=None):
        return rs.PlanarClosedCurveContainment(self.GUID, curve, plane, tolerance)

    def planarCollision(self, curve, plane=None, tolerance=None):
        return rs.PlaneCurveCollision(self.GUID, curve, plane, tolerance)

    def pointInside(self, point, plane=None, tolerance=None):
        # PointInPlanarClosedCurve
        return rs.PointInPlanarClosedCurve(point, self.GUID, plane, tolerance)

    def polyCount(self, segment_index=-1):
        #PolyCurve or PolyLine
        return rs.PolyCurveCount(self.GUID, segment_index)

    def vertices(self, index=-1):
        return rs.PolylineVerticies(self.GUID, index)

    def project(self, projection_object, direction):
        if rs.IsMesh(projection_object):
            return rs.ProjectCurveToMesh(self.GUID, projection_object, direction)
        if rs.IsSurface(projection_object):
            return rs.ProjectCurveToSurface(self.GUID, projection_object, direction)

    def rebuild(self, degree=3, point_count=10):
        return rs.RebuildCurve(self.GUID, degree, point_count)

    def removeKnot(self, parameter):
        return rs.RemoveCurveKnot(self.GUID, parameter)

    def reverse(self):
        return rs.ReverseCurve(self.GUID)

    def simplify(self, flags=0):
        return rs.SimplifyCurve(self.GUID, flags)

    def split(self, parameter, delete_input=True):
        return rs.SplitCurve(self.GUID, parameter, delete_input)

    def trim(self, interval, delete_input=True):
        return rs.TrimCurve(self.GUID, interval, delete_input)

class FilletCurve(Curve):
    def __init__(self, curves, parameters, reverses, continuities):
        self.GUID = self._add(curves, parameters, reverses, continuities)

    def _add(self, curves, parameters, reverses, continuities):
        return rs.BlendCurve(curves, parameters, reverses, continuities)

class InterpCurve(Curve):
    def __init__(self, points, degree=3, knotstyle=0, start_tangent=None, end_tangent=None):
        self.GUID = self._add(points, degree, knotstyle, start_tangent, end_tangent)

    def _add(self, points, degree=3, knotstyle=0, start_tangent=None, end_tangent=None):
        return rs.AddInterpCurve(points, degree, knotstyle, start_tangent, end_tangent)

class NurbsCurve(Curve):
    def __init__(self, points, knots, degree, weights=None):
        self.GUID = self._add(points, knots, degree, weights)

    def _add(self, points, knots, degree, weights=None):
        return rs.AddNurbsCurve(points, knots, degree, weights)

class PtCurve(Curve):
    def __init__(self, pt1, pt2, pt3):
        self.GUID = self._add(pt1, pt2, pt3)
        
    def _add(self, pt1, pt2, pt3):
        return rs.AddCurve3Pt(pt1, pt2, pt3)