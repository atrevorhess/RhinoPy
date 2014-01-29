import rhinoscriptsyntax as rs

class Polycurve:
    def __init__(self):
        pass

    def _isPolyCurve(self, obj, segment_index=-1):
        return rs.IsPolyCurve(obj, segment_index)

    def count():
        pass