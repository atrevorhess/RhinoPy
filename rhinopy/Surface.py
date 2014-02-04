import rhinoscriptsyntax as rs
from Curve import Curve

class Surface:
    def __init__(self):
        self.GUID = self._add()

    def _isBrep(self):
        return rs.IsBrep(self.GUID)

    def _isCone(self):
        return rs.IsCone(self.GUID)

    def _isCylinder(self):
        return rs.IsCylinder(self.GUID)

    def _isPlaneSurface(self):
        return rs.IsPlaneSurface(self.GUID)

    def _isPolysurface(self):
        return rs.IsPolysurface(self.GUID)

    """
    Polysurface Method
    def _isPolysurfaceClosed(self):
        pass
    """

    def _isSphere(self):
        return rs.IsSphere(self.GUID)

    def _isSurface(self):
        return rs.IsSurface(self.GUID)

    def _isTorus(self):
        return rs.IsTorus(self.GUID)

    def difference(self, surface, delete_input=True):
        #If delete input is true then both surfaces need to be delete (self and input surface, if false then method can return a new surface)
        return rs.BooleanDifference(self.GUID, surface.GUID, delete_input)

    def intersection(self, surface, delete_input=True):
        return rs.BooleanIntersection(self.GUID, surface.GUID, delete_input)

    def union(self, surfaces, delete_input=True):
        surfaces = [surface.GUID for surface in surfaces]
        surfaces.append(self.GUID)
        return rs.BooleanUnion(surfaces, delete_input)

    def closestPoint(self, point):
        return rs.BrepClosestPoint(self.GUID, point)

    def capPlanarHoles(self):
        return rs.CapPlanarHoles(self.GUID)

    def duplicateEdgeCurves(self, select=False):
        return [Curve(curve) for curve in rs.DuplicateEdgeCurves(self.GUID, select)]

    def duplicateBorder(self):
        return [Curve(curve) for curve in rs.DuplicateSurfaceBorder(self.GUID)]

    def evaluate(self, u, v):
        return rs.EvaluateSurface(self.GUID, u, v)

    """
    def explodePolysurfaces(self):
        pass
    """

    def extend(self, parameter, length, smooth=True):
        return rs.ExtendSurface(self.GUID, parameter, length, smooth)

    def extractIsoCurve(self, parameter, direction):
        return [Curve(curve) for curve in rs.ExtraceIsoCurve(self.GUID, parameter, direction)]

    def extract(self, face_indicies, copy=False):
        return [Surface(surface) for surface in rs.ExtractSurface(self.GUID, face_indicies, copy)]

    """
    Curve Method
    def ExtrudeCurve(self):
        pass
    
    def ExtrudeCurvePoint(self):
        pass

    def ExtrudeCurveStraight(self):
        pass
    """

    def fillet(self, surface, radius, uv_param0=None, uv_param1=None):
        return [Surface(srf) for srf in rs.FilletSurfaces(self.GUID, surface.GUID, radius, uv_param0, uv_param1)]

    def flip(self, flip=None):
        return rs.FlipSurface(self.GUID, flip)

    """
    def IntersectBreps(self):
        pass
    """

    def isPointInSurface(self):
        return rs.IsPointInSurface(self.G)

    def isPointOnSurface(self):
        pass

    def isSurfaceClosed(self):
        pass

    def isSurfacePeriodic(self):
        pass

    def isSurfacePlanar(self):
        pass

    def isSurfaceRational(self):
        pass

    def isSurfaceSingular(self):
        pass

    def isSurfaceTrimmed(self):
        pass

    def join(self, objects, delete_input=False):
        return rs.JoinSurfaces(self.GUID, objects)

    def makePeriodic(self, direction, delete_input):
        if (delete_input):
            self.GUID = rs.MakeSurfacePeriodic(self.GUID, direction, delete_input)
        else:
            return rs.MakeSurfacePeriodic(self.GUID, direction, delete_input)

    def offset(self, distance, tolerance=None, both_sides=False, create_solid=False):
        return Surface(rs.OffsetSurface(self.GUID, distance, tolerance, both_sides, create_solid))

    """
    Curve Method
    def PullCurve(self):
        pass
    """

    def rebuild(self, degree=(3,3), pointcount=(10,10)):
        return rs.RebuildSurface(self.GUID, degree=(3,3), pointcount=(10,10))

    # def shootRay(self):
    #     pass

    def shortPath(self, start_point, end_point):
        return Curve(rs.ShortPath(self.GUID, start_point, end_point))

    def shrink(self):
        # test for isSurfaceTrimmed
        pass

    def split(self):
        # check for isBrep
        pass

    def area(self):
        pass

    def centroid(self):
        pass

    def areaMoments(self):
        pass

    """
    Cone method
    def SurfaceCone(self):
        pass
    """

    # def SurfaceClosestPoint(self):
        # Duplicate Method
        # pass

    def curvature(self):
        pass

    """
    Cylinder Method
    def SurfaceCylinder(self):
        pass
    """

    def degree(self):
        pass

    def domain(self):
        pass

    def editPoints(self):
        pass

    # def evaluate(self):
    #     Duplicate Method
    #     pass

    def frame(self):
        pass

    def isocurveDensity(self):
        pass

    def knotCount(self):
        pass

    def knots(self):
        pass

    def normal(self):
        pass

    def normalizedParameter(self):
        pass

    def parameter(self):
        pass

    def pointCount(self):
        pass

    def points(self):
        pass

    def torus(self):
        pass

    def volume(self):
        #test isClosed
        pass

    def volumeCentroid(self):
        # combine with area centroid
        # test isClosed or isBrep
        pass

    def volumeMoments(self):
        #combine with area moments
        pass

    def weights(self):
        pass

    def TrimBrep(self):
        # test isBrep
        pass

    def trim(self):
        pass

    def unroll(self):
        pass

#Abstract Surface Classes

class Box(Surface):
    def __init__(self, corners):
        self.GUID = self._add(corners)

    def _add(self, corners):
        return rs.AddBox(corners)

class Cone(Surface):
    def __init__(self, base, height, radius, cap=True):
        self.GUID = self._add(base, height, radius, cap)

    def _add(self, base, height, radius, cap=True):
        return rs.AddCone(base, height, radius, cap)

class CutPlane(Surface):
    def __init__(self, object_ids, start_point, end_point, normal=None):
        self.GUID = self._add(object_ids, start_point, end_point, normal)

    def _add(self, object_ids, start_point, end_point, normal=None):
        return rs.AddCupPlane(object_ids, start_point, end_point, normal)

class Cylinder(Surface):
    def __init__(self, base, height, radius, cap=True):
        self.GUID = self._add(base, height, radius, cap)

    def _add(self, base, height, radius, cap=True):
        return rs.AddCylinder(base, height, radius, cap)

class EdgeSrf(Surface):
    def __init__(self, curves):
        self.GUID = self._add(curves)

    def _add(self, curves):
        return rs.AddEdgeSrf(curves)

class LoftSrf(Surface):
    def __init__(self, object_ids, start=None, end=None, loft_type=0, simplify_method=0, value=0, closed=False):
        self.GUID = self._add(object_ids, start, end, loft_type, simplify_method, value, closed)

    def _add(self, object_ids, start=None, end=None, loft_type=0, simplify_method=0, value=0, closed=False):
        return rs.AddLoftSrf(object_ids, start, end, loft_type, simplify_method, value, closed)

class NurbsSrf(Surface):
    def __init__(self, point_count, points, knots_u, knots_v, degree, weights=None):
        self.GUID = self._add(point_count, points, knots_u, knots_v, degree, weights)

    def _add(self, point_count, points, knots_u, knots_v, degree, weights=None):
        return rs.AddNurbsSurface(point_count, points, knots_u, knots_v, degree, weights)

class Pipe(Surface):
    def __init__(self, curve_id, parameters, radii, blend_type=0, cap=0, fit=False):
        self.GUID = self._add(curve_id, parameters, radii, blend_type, cap, fit)

    def _add(self, curve_id, parameters, radii, blend_type=0, cap=0, fit=False):
        return rs.AddPipe(curve_id, parameters, radii, blend_type, cap, fit)

class PlanarSrf(Surface):
    def __init__(self, objects):
        self.GUID = self._add(objects)

    def AddPlanarSrf(self, objects):
        return rs.AddPlanarSrf(objects)

class PlaneSrf(Surface):
    def __init__(self, plane, u_direction, v_direction):
        self.GUID = self._add(plane, u_direction, v_direction)

    def _add(self, plane, u_direction, v_direction):
        return rs.AddPlaneSurface(plane, u_direction, v_direction)

class RevSrf(Surface):
    def __init__(self, curve_id, axis, start_angle=0.0, end_angle=360.0):
        self.GUID = self._add(curve_id, axis, start_angle, end_angle)

    def _add(self, curve_id, axis, start_angle=0.0, end_angle=360.0):
        return rs.AddRevSrf(curve_id, axis, start_angle, end_angle)

class Sphere(Surface):
    def __init__(self, center_or_plane, radius):
        self.GUID = self._add(center_or_plane, radius)

    def _add(self, center_or_plane, radius):
        return rs.AddSphere(center_or_plane, radius)

    def IntersectSpheres(self):
        pass

"""
SrfContourCrvs
SrfControlPtGrid
SrfPt
SrfPtGrid
"""

#Combine the two sweeps in future revisions
class Sweep1(Surface):
    def __init__(self, rail, shapes, closed=False):
        self.GUID = self._add(rail, shapes, closed)

    def _add(self, rail, shapes, closed=False):
        return rs.AddSweep1(rail, shapes, closed)

class Sweep2(Surface):
    def __init__(self, rails, shapes, closed=False):
        self.GUID = self._add(rails, shapes, closed)

    def _add(self, rails, shapes, closed=False):
        return rs.AddSweep2(rails, shapes, closed)

class Torus(Surface):
    def __init__(self, base, major_radius, minor_radius, direction=None):
        self.GUID = self._add(base, major_radius, minor_radius, direction)

    def _add(self, base, major_radius, minor_radius, direction=None):
        return rs.AddTorus(base, major_radius, minor_radius, direction)