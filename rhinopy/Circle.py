import rhinoscriptsyntax as rs
from Curve import CurveObject
from Point import PointObject

class CircleObject(CurveObject):
    def __init__(self, guid):
        CurveObject.__init__(self, guid)

    def IsCircle(self, obj, segment_index=-1):
        return rs.IsCircle(obj, segment_index)

    def centerPoint(self, segment_index=-1, return_plane=False):
        if return_plane == True:
            return rs.CircleCenterPoint(self.GUID, segment_index, return_plane)
        else:
            return PointObject(rs.CircleCenterPoint(self.GUID, segment_index, return_plane))

    def circumference(self, segment_index=-1):
        return rs.CircleCircumference(self.GUID, segment_index)

    def radius(self, segment_index=-1):
        return rs.CircleRadius(self.GUID, segment_index)

class Circle(CircleObject):
    def __init__(self, plane_or_center, radius, hidden=False, locked=False, selected=False):
        self.GUID = self._add(plane_or_center, radius)

    def _add(self, plane_or_center, radius):
        return rs.AddCircle(plane_or_center, radius)

class PtCircle(CircleObject):
    def __init__(self, pt1, pt2, pt3):
        self.GUID = self._add(pt1, pt2, pt3)

    def _add(self, pt1, pt2, pt3):
        return rs.AddCircle3Pt(pt1, pt2, pt3)