import rhinoscriptsyntax as rs
from Circle import Circle

class PtCircle(Circle):
    def __init__(self, pt1, pt2, pt3):
        self.GUID = self._add(pt1, pt2, pt3)

    def _add(self, pt1, pt2, pt3):
        return rs.AddCircle3Pt(pt1, pt2, pt3)
