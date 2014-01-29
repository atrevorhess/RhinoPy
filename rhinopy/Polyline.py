import rhinoscriptsyntax as rs

class Polyline:
    def __init__(self):
        pass

    def _isPolyline(self, obj, segment_index=-1):
        return rs.IsPolyline(obj, segment_index)
        
    def verticies():
        pass