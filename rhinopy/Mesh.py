import rhinoscriptsyntax as rs
from Object import Object
from Curve import CurveObject
from Point import PointObject
from Vector import VectorObject

class MeshObject(Object):
    def __init__(self, guid):
        Object.__init__(self, guid)

    def _isMesh(self, obj):
        return rs.IsMesh(obj.GUID)

    def CurveMeshIntersection(self):
        pass

    def disjointMeshCount(self):
        return rs.DisjointMeshCount(self.GUID)

    def duplicateMeshBorder(self):
        return [CurveObject(curve) for curve in rs.DuplicateMeshBorder(self.GUID)]

    def explode(self):
        return [MeshObject(mesh) for mesh in rs.ExplodeMeshes(self.GUID)]

    def isClosed(self):
        return rs.IsMeshClosed(self.GUID)

    def isManifold(self):
        return rs.IsMeshManifold(self.GUID)

    def isPointOnMesh(self, point):
        return rs.IsPointOnMesh(self.GUID, point.GUID)

    def join(self, meshes, delete_input=False):
        mesh_id_list = [mesh.GUID for mesh in meshes]
        joined_mesh_guid = rs.JoinMeshes(mesh_id_list, delete_input)
        if delete_input:
            pass
        return Mesh(joined_mesh_guid)

    def area(self):
        return rs.MeshArea(self.GUID)

    def areaCentroid(self):
        return PointObject(rs.MeshAreaCentroid(self.GUID))

    def booleanDifference(self, difference_mesh, delete_input=True):
        return [MeshObject(mesh) for mesh in rs.MeshBooleanDifference(self.GUID, difference_mesh.GUID, delete_input)]

    def booleanIntersection(self, intersection_mesh, delete_input=True):
        return [MeshObject(mesh) for mesh in rs.MeshBooleanIntersection(self.GUID, intersection_mesh.GUID, delete_input)]

    def booleanSplit(self, split_mesh, delete_input=True):
        return [MeshObject(mesh) for mesh in rs.MeshBooleanSplit(self.GUID, split_mesh.GUID, delete_input)]

    def booleanUnion(self, union_mesh, delete_input=True):
        return [MeshObject(mesh) for mesh in rs.MeshBooleanUnion(self.GUID, union_mesh.GUID, delete_input)]

    def closestPoint(self, point, maximum_distance):
        return rs.MeshClosestPoint(self.GUID, point, maximum_distance)

    def faceCenters(self):
        return [PointObject(point) for point in rs.MeshFaceCenters(self.GUID)]

    def faceCount(self):
        return rs.MeshFaceCount(self.GUID)

    def faceNormals(self):
        return [VectorObject(vector) for vector in rs.MeshFaceNormals(self.GUID)]

    def faces(self, face_type=True):
        return [PointObject(point) for point in rs.MeshFaces(self.GUID, face_type)]

    def faceVertices(self):
        return rs.MeshFaceVerticies(self.GUID)

    def hasFaceNormals(self):
        return rs.MeshHasFaceNormals(self.GUID)

    def hasTextureCoordinates(self):
        return rs.MeshHasTextureCoordinates(self.GUID)

    def hasVertexColors(self):
        return rs.MeshHasVertexColors(self.GUID)

    def hasVertexNormals(self):
        return rs.MeshHasVertexNormals(self.GUID)

    def MeshMeshIntersection(self, mesh, tolerance=None):
        return rs.MeshMeshInteresection(self.GUID, mesh.GUID, tolerance)

    def nakedEdgePoints(self):
        return rs.MeshNakedEdgePoints(self.GUID)

    def offset(self, distance):
        return MeshObject(rs.MeshOffest(self.GUID, distance))

    def outline(self, view=None):
        # Returns Polyline Curves if successful
        return rs.MeshOutline(self.GUID, view)

    def quadCount(self):
        return rs.MeshQuadCount(self.GUID)

    def quadsToTriangles(self):
        return rs.MeshQuadsToTrinagles(self.GUID)

    def toNurb(self, trimmed_triangles=True, delete_input=False):
        """
        Warning: This method converts each polygon face to a NURBS surface. It is not meant to convert entire mesh models to NURBS models and there is, in fact, no simple way to accomplish this.
        """
        return rs.MeshToNurb(self.GUID, trimmed_triangles, delete_input)

    def triangleCount(self):
        return rs.MeshTriangleCount(self.GUID)

    def vertexColors(self, colors=0):
        return rs.MeshVertexColors(self.GUID, colors)

    def vertexCount(self):
        return rs.MeshVertexCount(self.GUID)

    def vertexFaces(self, vertex_index):
        return rs.MeshVertexFaces(self.GUID, vertex_index)

    def vertexNormals(self):
        return [VectorObject(vector) for vector in rs.MeshVertexNormals(self.GUID)]

    def vertices(self):
        return [PointObject(point) for point in rs.MeshVertices(self.GUID)]

    def volume(self):
        return rs.MeshVolume(self.GUID)

    def volumeCentroid(self):
        return PointObject(rs.MeshVolumeCentroid(self.GUID))

    def pullCurve(self, curve):
        return CurveObject(rs.PullCurveToMesh(self.GUID, curve.GUID))

    def splitDisjoint(self, delete_input=False):
        return [MeshObject(mesh) for mesh in rs.SplitDisjointMesh(self.GUID, delete_input)]

    def unifyNormals(self):
        return rs.UnifyMeshNormals(self.GUID)

class Mesh(MeshObject):
    def __init__(self, vertices, face_vertices, vertex_normals=None, texture_coordinates=None, vertex_colors=None):
        MeshObject.__init__(self, self._add(vertices, face_vertices, vertex_normals, texture_coordinates, vertex_colors))
    
    def _add(self, vertices, face_vertices, vertex_normals=None, texture_coordinates=None, vertex_colors=None):
        return rs.AddMesh ( vertices, face_vertices, vertex_normals, texture_coordinates, vertex_colors)

class PlanarMesh(MeshObject):
    def __init__(self, planar_curve, delete_input=False):
        MeshObject.__init__(self, self._add(planar_curve, delete_input))

    def _add (self, planar_curve, delete_input=False):
        return rs.AddPlanarMesh(planar_curve, delete_input)