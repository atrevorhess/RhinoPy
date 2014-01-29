import rhinoscriptsyntax as rs
from Curve import Curve

class InterpCurve(Curve):
    def __init__(self, points, degree=3, knotstyle=0, start_tangent=None, end_tangent=None):
        self.GUID = self._add(points, degree, knotstyle, start_tangent, end_tangent)

    def _add(self, points, degree=3, knotstyle=0, start_tangent=None, end_tangent=None):
        return rs.AddInterpCurve(points, degree, knotstyle, start_tangent, end_tangent)