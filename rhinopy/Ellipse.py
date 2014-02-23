import rhinoscriptsyntax as rs
from Curve import CurveObject
from Point import PointObject

class Ellipse(CurveObject):
    def __init__(self, plane, radius_x, radius_y, hidden=False, locked=False, selected=False):
        CurveObject.__init__(self, self._add(plane, radius_x, radius_y))

    def _add(self, plane, radius_x, radius_y):
        return rs.AddEllipse(plane, radius_x, radius_y)

    def _isEllipse(self, obj):
        return rs.IsEllipse(obj)

    def centerPoint(self):
        return PointObject(rs.EllipseCenterPoint(self.GUID))

    def quadPoints(self):
        return [PointObject(point) for point in rs.EllipseQuadPoints(self.GUID)]