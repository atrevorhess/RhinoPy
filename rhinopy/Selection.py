import rhinoscriptsyntax as rs

class Selection:
    def __init__(self):
        pass

    def selectAll(self, select=False, include_lights=False, include_grips=False):
        return rs.AllObjects(select, include_lights, include_grips)

    def selectFirst(self, select=False, include_lights=False, include_grips=False):
        return rs.FirstObject(select, include_lights, include_grips)

    def getCurve(self, message=None, preselect=False, select=False):
        return rs.GetCurveObject(message, preselect, select)

    def getObject(self, message=None, selection_filter=0, preselect=False, select=False, custom_filter=None, subobjects=False):
        return rs.GetObject(message, selection_filter, preselect, select=False, custom_filter, subobjects)

    def getObjectEx(self, message=None, selection_filter=0, preselect=False, select=False, objects=None):
        return rs.GetObjectEx(message, selection_filter, preselect, select, objects)

    def getObjects(self, message=None, selection_filter=0, group=True, preselect=False, select=False, objects=None, minimum_count=1, maximum_count=0, custom_filter=None):
        return rs.GetObjects(message, selection_filter, group, preselect, select, objects, minimum_count, maximum_count, custom_filter)

    def getObjectsEx(self, message=None, selection_filter=0, group=True, preselect=False, select=False, objects=None):
        return rs.GetObjectsEx(message, selection_filter, group, preselect, select, objects)

    def getPointCoordinates(self, message="selectpoints", preselect=False):
        return rs.GetPointCoordinates(message, preselect)

    def getSurfaceObject(self, message="select surface", preselect=False, select=False):
        return rs.GetSurfaceObject(message, preselect, select)

    def hiddenObjects(self, include_lights=False, include_grips=False):
        return rs.hiddenObjects(include_lights, include_grips)

    def invertSelectedObjects(self, include_lights=False, include_grips=False):
        return rs.InvertSelectedObjects(include_lights, include_grips)

    def lastCreatedObjects(self, select=False):
        return rs.LastCreatedObjects(select)

    def lastObject(self, select=False, include_lights=False, include_grips=False):
        return rs.LastObject(select, include_lights, include_grips)

    def lockedObjects(self, include_lights=False, include_grips=False):
        return rs.LockedObjects(include_lights, include_grips)

    def nextObject(self, object_id, select=False, include_lights=False, include_grips=False):
        return rs.NextObject(object_id.GUID, select, include_lights, include_grips)

    def normalObjects(self, include_lights=False, include_grips=False):
        return rs.NormalObjects(include_lights, include_grips)

    def byColor(self, color, select=False, include_lights=False):
        return rs.ObjectsByColor(color, select, include_lights)

    def byGroup(self, group_name, select=False):
        return rs.ObjectsByGroup(group_name, select)

    def byLayer(self, layer_name, select=False):
        return rs.ObjectsByLayer(layer_name, select)

    def byName(self, name, select=False, include_lights=False):
        return rs.ObjectsByName(name, select, include_lights)

    def byType(self, type, select=False, state=0):
        return rs.ObjectsByType(type, select, state)

    def selectedObjects(self, include_lights=False, include_grips=False):
        return rs.SelectedObjects(include_lights=False, include_grips=False)

    def unselectAllObjects(self):
        return rs.UnselectAllObjects()
