import rhinoscriptsyntax as rs
from Curve import Curve
from Point import Point

class Ellipse(Curve):
    def __init__(self, plane, radius_x, radius_y, hidden=False, locked=False, selected=False):
        self.GUID = self._add(plane, radius_x, radius_y)

    def _add(self, plane, radius_x, radius_y):
        return rs.AddEllipse(plane, radius_x, radius_y)

    def centerPoint(self):
        return Point(rs.EllipseCenterPoint(self.GUID))

    def quadPoints(self):
        points = [Point(point) for point in rs.EllipseQuadPoints(self.GUID)]
        return points