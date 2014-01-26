import rhinoscriptsyntax as rs

class Interface:
    def selectFolder():
        return rs.BrowseForFolder(folder=None, message=None, title=None)

    def selectItems(items, message=None, title=None):
        pass

    def EditBox():
        pass

    def getAngle(point=None, reference_point=None, default_angle_degrees=0):
        pass

    def getBoolean(message, items, defaults):
        pass

    def getBox(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None):
        pass

    def getColor(color=[0,0,0]):
        pass

    def getInteger(message=None, number=None):
        pass

    def getLayer(title="Select Layer", layer=None, show_new_button=False):
        pass

    def getMeshFaces(mesh, message="", min_count=1, max_count=0):
        pass

    def getMeshVertices(mesh, message="", min_count=1, max_count=0):
        pass

    def getPoint(message=None, base_point=None, distance=None, in_plane=False):
        pass

    def getPointOnCurve(curve, message=None):
        pass

    def getPointOnMesh(mesh, message=None):
        pass

    def getPointOnSurface(surface, message=None):
        pass

    def getPoints(draw_lines=False, in_plane=False, message1=None, message2=None, max_points=None, base_point=None):
        pass

    def getReal(message=None, number=None, minimum=None, maximum=None):
        pass

    def getRectangle(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None):
        pass

    def getString(message=None, default_string=None, strings=None):
        pass

    def displayItems(items, message=None, title=None, default=None):
        pass

    def displayMessage(message, buttons=0, title=None):
        pass

    def openFileName(title=None, filter=None, folder=None, file_name=None, extension=None):
        pass

    def OpenFileNames(title=None, filter=None, folder=None, file_name=None, extension=None):
        pass

    def PopupMenu(items, modes=None, point=None, view=None):
        pass

    def PropertyListBox(items, values, message=None, title=None):
        pass

    def RealBox(message=None, default_number=None, title=None, minimum=None, maximum=None):
        pass

    def SaveFileName(title=None, filter=None, folder=None, file_name=None, extension=None):
        pass

    def StringBox(message=None, default_value=None, title=None):
        pass