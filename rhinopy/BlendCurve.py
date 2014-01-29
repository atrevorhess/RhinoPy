import rhinoscriptsyntax as rs
from Curve import Curve

class FilletCurve(Curve):
    def __init__(self, curves, parameters, reverses, continuities):
        self.GUID = self._add(curves, parameters, reverses, continuities)

    def _add(self, curves, parameters, reverses, continuities):
        return rs.BlendCurve(curves, parameters, reverses, continuities)