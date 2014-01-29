import rhinoscriptsyntax as rs
from Curve import Curve

class NurbsCurve(Curve):
    def __init__(self, points, knots, degree, weights=None):
        self.GUID = self._add(points, knots, degree, weights)

    def _add(self, points, knots, degree, weights=None):
        return rs.AddNurbsCurve(points, knots, degree, weights)