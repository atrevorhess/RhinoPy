import rhinoscriptsyntax as rs
from Point import Point

class PolarPoint(Point):
    def __init__(self, origin, angle_degrees, distance, plane=None, hidden=False, locked=False, selected=False):
        self.GUID = rs.Polar(origin, angle_degrees, distance, plan=None)