import rhinoscriptsyntax as rs
from Object import Object

class Mesh(Object):
    def __init__(self, vertices, face_vertices, vertex_normals=None, texture_coordinates=None, vertex_colors=None):
        self.GUID = self._draw(vertices, face_vertices, vertex_normals, texture_coordinates, vertex_colors)
    
    def _draw(self, vertices, face_vertices, vertex_normals=None, texture_coordinates=None, vertex_colors=None):
        return rs.AddMesh ( vertices, face_vertices, vertex_normals, texture_coordinatese, vertex_colors)

    def AddPlanarMesh(self):
        pass

    def CurveMeshIntersection(self):
        pass

    def DisjointMeshCount(self):
        pass

    def DuplicateMeshBorder(self):
        pass

    def ExplodeMeshes(self):
        pass

    def IsMesh(self):
        pass

    def IsMeshClosed(self):
        pass

    def IsMeshManifold(self):
        pass

    def IsPointOnMesh(self):
        pass

    def JoinMeshes(self):
        pass

    def MeshArea(self):
        pass

    def MeshAreaCentroid(self):
        pass

    def MeshBooleanDifference(self):
        pass

    def MeshBooleanIntersection(self):
        pass

    def MeshBooleanSplit(self):
        pass

    def MeshBooleanUnion(self):
        pass

    def MeshClosestPoint(self):
        pass

    def MeshFaceCenters(self):
        pass

    def MeshFaceCount(self):
        pass

    def MeshFaceNormals(self):
        pass

    def MeshFaces(self):
        pass

    def MeshFaceVertices(self):
        pass

    def MeshHasFaceNormals(self):
        pass

    def MeshHasTextureCoordinates(self):
        pass

    def MeshHasVertexColors(self):
        pass

    def MeshHasVertexNormals(self):
        pass

    def MeshMeshIntersection(self):
        pass

    def MeshNakedEdgePoints(self):
        pass

    def MeshOffset(self):
        pass

    def MeshOutline(self):
        pass

    def MeshQuadCount(self):
        pass

    def MeshQuadsToTriangles(self):
        pass

    def MeshToNurb(self):
        pass

    def MeshTriangleCount(self):
        pass

    def MeshVertexColors(self):
        pass

    def MeshVertexCount(self):
        pass

    def MeshVertexFaces(self):
        pass

    def MeshVertexNormals(self):
        pass

    def MeshVertices(self):
        pass

    def MeshVolume(self):
        pass

    def MeshVolumeCentroid(self):
        pass

    def PullCurveToMesh(self):
        pass

    def SplitDisjointMesh(self):
        pass

    def UnifyMeshNormals(self):
        pass