import rhinoscriptsyntax as rs
from Curve import Curve

class FilletCurve(Curve):
    def __init__(self, curve0id, curve1id , radius=1.0, base_point0=None, base_point1=None):
        self.GUID = self._add(curve0id, curve1id , radius, base_point0, base_point1)

    def _add(self, curve0id, curve1id , radius, base_point0, base_point1):
        return rs.BlendCurve(curve0id, curve1id , radius, base_point0, base_point1)