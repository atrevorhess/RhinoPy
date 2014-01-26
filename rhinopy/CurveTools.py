import rhinoscriptsyntax as rs
from Point import Point

"""
File contains a list of methods that can act on both lines and curves
Created to prevent code duplication
All methods need to be tested on lines, were included in curve functions
"""

# arrows
def arrows(self, arrow_style=None):
    """
    Toggles a curve object's annotation arrows.
    If a style is specified the method returns the previous annotation style if successful. If a style is not specified the method returns the current annotation style.
    If not successful, or on an error, the method returns None
    """
    return rs.CurveArrows(self.GUID, arrow_style)

# booleanDifference
def booleanDifference(self, curve):
    """
    Calculates the difference between self and another curve the results to the document.
    Curves must be coplanar.
    If successful the method returns a list of new objects
    If unsuccessful the method returns None
    """
    return rs.CurveBooleanDifference(self.GUID, curve)

# booleanIntersection
def booleanInteresection(self, curve):
    """
    Calculates the intersection between self and another curve the results to the document.
    Curves must be coplanar.
    If successful the method returns a list of new objects
    If unsuccessful the method returns None
    """
    return rs.CurveBooleanIntersection(self.GUID, curve)

# booleanUnion
def booleanUnion(self, curve):
    """
    Calculates the union between self and another curve the results to the document.
    Curves must be coplanar.
    If successful the method returns a list of new objects
    If unsuccessful the method returns None
    """
    return rs.CurveBooleanUnion(self.GUID, curve)

# deviation
def deviation(self, curve):
    return rs.CurveDeviation(self.GUID, curve)

# directionsMatch
def directionsMatch(self, curve):
    return rs.CurveDirectionsMatch(self.GUID, curve)

# endPoints
def endPoints(self):
    #return start and end points
    return [Point(rs.CurveStartPoint(self.GUID)), Point(rs.CurveEndPoint(self.GUID))]

# length
def length(self, segment_index=-1, sub_domain=None):
        return rs.CurveLength(self.GUID, segment_index, sub_domain)
# midpoint
def midpoint(self, segment_index=-1):
    return rs.CurveMidPoint(self.GUID, segment_index)

# divide
def divide(self, segments, create_points=False, return_points=True):
    return rs.DivideCurve(self.GUID, segments, create_points, return_points)

# divideEquidistant
def divideEquidistant(self, distance, create_points=False, return_points=True):
    return rs.DivideCurveEquidistant(self.GUID, distance, create_points, return_points)

# divideLength
def divideLength(self, length, create_points=False, return_points=True):
    return rs.DivideCurveLength(self.GUID, length, create_points, return_points=True)

# extend
def extend(self, extension_type, side, boundary_object_ids):
    return rs.ExtendCurve(self.GUID, extension_type, side, boundary_object_ids)

# extendLength
def extendLength(self, extension_type, side, length):
    return rs.ExtendCurveLength(self.GUID, extension_type, side, length)

# join
def join(self, curves, delete_input=False, tolerance=None):
        return rs.JoinCurves(curves.append(self.GUID), delete_input, tolerance)

# offset
def offset(self, direction, distance, normal=None, style=1):
    return rs.OffsetCurve(self.GUID, direction, distance, normal, style)

# offsetOnSurface
def offsetOnSurface(self, surface, distance_or_parameter):
    return rs.OffsetCurveOnSurface(self.GUID, surface, distance_or_parameter)

# PlanarClosedContainment
def planarClosedContainment(self, curve, plane=None, tolerance=None):
    return rs.PlanarClosedCurveContainment(self.GUID, curve, plane, tolerance)

# planarColisions
def planarCollision(self, curve, plane=None, tolerance=None):
    return rs.PlaneCurveCollision(self.GUID, curve, plane, tolerance)

# project
def project(self, projection_object, direction):
    if rs.IsMesh(projection_object):
        return rs.ProjectCurveToMesh(self.GUID, projection_object, direction)
    if rs.IsSurface(projection_object):
        return Curev(rs.ProjectCurveToSurface(self.GUID, projection_object, direction)

# reverse
def reverse(self):
    self.GUID = rs.ReverseCurve(self.GUID)

# split
def split(self, parameter, delete_input=True):
    return rs.SplitCurve(self.GUID, parameter, delete_input)

# trim
def trim(self, interval, delete_input=True):
    self.GUID = rs.TrimCurve(self.GUID, interval, delete_input)
