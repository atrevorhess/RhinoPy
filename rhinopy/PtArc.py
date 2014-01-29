import rhinoscriptsyntax as rs
from Arc import Arc

class PtArc(Arc):
    def __init__(self, start_point, end_point, point_on_arc):
        self.GUID = self._add(start_point, end_point, point_on_arc)

    def _add(self, start_point, end_point, point_on_arc):
        return rs.AddArc3Pt(start_point, end_point, point_on_arc)