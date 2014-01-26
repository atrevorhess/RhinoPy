import rhinoscriptsyntax as rs

class Vector:
    def __init__(self, points):
        self.GUID = self._add(points)

    def _add(self, points):
        return rs.VectorCreate(points[0], points[1])

    def isParallelTo(self, vector):
        return rs.IsVectorParallelTo(self.GUID, vector.GUID)

    def isPerpendicularTo(self, vector):
        return rs.IsVectorPerpendicularTo(self.GUID, vector.GUID)

    def isTiny(self):
        return rs.IsVectorTiny(self.GUID)

    def isZero(self):
        return rs.IsVectorZero(self.GUID)

    def add(self, vector):
        return Vector(rs.VectorAdd(self.GUID, vector.GUID))

    def angle(self, vector):
        return rs.VectorAngle(self.GUID, vector.GUID)

    def compare(self, vector):
        return rs.VectorCompare(self.GUID, vector.GUID)
        
    def crossProduct(self, vector):
        return Vector(rs.VectorCrossProduct(self.GUID, vector.GUID))

    def divide(self, divide):
        self.GUID = rs.VectorDivide(self.GUID, divide)

    def dotProduct(self, vector):
        return rs.VectorDotProduct(self.GUID, vector.GUID)

    def length(self):
        return rs.VectorLength(self.GUID)

    def multiply(self, vector):
        return rs.VectorMultiply(self.GUID, vector.GUID)

    def reverse(self):
        self.GUID = rs.VectorReverse(self.GUID)

    def rotate(self, angle_degrees, axis):
        self.GUID = rs.VectorRotate(self.GUID, angle_degrees, axis)

    def scale(self, scale):
        self.GUID = rs.VectorScale(self.GUID, scale)

    def subtract(self, vector):
        return Vector(rs.VectorSubtract(self.GUID, vector.GUID))

    def transform(self, xform):
        self.GUID = rs.VectorTransform(self.GUID, xform)

    def unitize(self):
        self.GUID = rs.VectorUnitize(self.GUID)