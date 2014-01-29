import rhinoscriptsyntax as rs
from Arc import Arc

class TanArc(Arc):
    def __init__(self, start_point, direction, end_point):
        self.GUID = self._add(start_point, direction, end_point)

    def _add(self, start_point, direction, end_point):
        return rs.AddArcPtTanPt(start_point, direction, end_point)