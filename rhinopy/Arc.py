import rhinoscriptsyntax as rs
from Curve import CurveObject
from Point import PointObject

class ArcObject(CurveObject):
    def __init__(self, guid):
        CurveObject.__init__(self, guid)

    def _isArc(self, obj, segment_index=-1):
        return rs.IsArc(obj, segment_index)

    def angle(self, segment_index=-1):
        return rs.ArcAngle(self.GUID, segment_index)

    def centerPoint(self, segment_index=-1):
        return PointObject(rs.ArcCenterPoint(self.GUID, segment_index))

    def midPoint(self, segment_index):
        return PointObject(rs.ArcMidPoint(self.GUID, segment_index))

    def radius(self, segment_index=-1):
        return rs.ArcRadius(self.GUID, segment_index)

class Arc(ArcObject):
    def __init__(self, plane, radius, degree, hidden=False, locked=False, selected=False):
        ArcObject.__init__(self, self._add(plane, radius, degree))

    def _add(self, plane, radius, degree):
        return rs.AddArc(plane, radius, degree)

class PtArc(ArcObject):
    def __init__(self, start_point, end_point, point_on_arc):
        ArcObject.__init__(self, self._add(start_point, end_point, point_on_arc))

    def _add(self, start_point, end_point, point_on_arc):
        return rs.AddArc3Pt(start_point, end_point, point_on_arc)

class TanArc(ArcObject):
    def __init__(self, start_point, direction, end_point):
        ArcObject.__init__(self, self._add(start_point, direction, end_point))

    def _add(self, start_point, direction, end_point):
        return rs.AddArcPtTanPt(start_point, direction, end_point)