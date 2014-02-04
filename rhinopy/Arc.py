import rhinoscriptsyntax as rs
from Curve import Curve
from Point import Point

class Arc(Curve):
    def __init__(self, plane, radius, degree, hidden=False, locked=False, selected=False):
        self.GUID = self._add(plane, radius, degree)

    def _add():
        pass

    def _isArc(self, obj, segment_index=-1):
        return rs.IsArc(obj, segment_index)

    def angle(self, segment_index=-1):
        return rs.ArcAngle(self.GUID, segment_index)

    def centerPoint(self, segment_index=-1):
        return Point(rs.ArcCenterPoint(self.GUID, segment_index))

    def midPoint(self, segment_index):
        return Point(rs.ArcMidPoint(self.GUID, segment_index))

    def radius(self, segment_index=-1):
        return rs.ArcRadius(self.GUID, segment_index)

class PtArc(Arc):
    def __init__(self, start_point, end_point, point_on_arc):
        self.GUID = self._add(start_point, end_point, point_on_arc)

    def _add(self, start_point, end_point, point_on_arc):
        return rs.AddArc3Pt(start_point, end_point, point_on_arc)

class TanArc(Arc):
    def __init__(self, start_point, direction, end_point):
        self.GUID = self._add(start_point, direction, end_point)

    def _add(self, start_point, direction, end_point):
        return rs.AddArcPtTanPt(start_point, direction, end_point)