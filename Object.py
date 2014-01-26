import rhinoscriptsyntax as rs

class Object:
    def __init__(self, guid, hidden=False, locked=False, selected=False):
        self.GUID = guid
        #Add commands to hide, lock, or select object is they are passed as true

    def __del__(self):
        self.delete()

    def __get__(self):
        return self.GUID
        
    def __getattr__(self):
        return self.GUID

    def __repr__(self):
        return self.GUID

    def __str__(self):
        return self.GUID

    def color(self, color=None):
        return rs.ObjectColor(self.GUID, color)
        
    def colorSource(self, source=None):
        return rs.ObjectColorSource(self.GUID, source)

    def copy(self, translation=None):
        return rs.CopyObject(self.GUID, translation)

    def delete(self): #Need to delete self when deleting the Object
        return rs.DeleteObject(self.GUID)

    def description(self):
        return rs.ObjectDescription(self.GUID)

    def flash(self):
        rs.FlashObject(self.GUID)

    def groups(self):
        return rs.ObjectGroups(self.GUID)
    
    def hide(self):
        return rs.HideObject(self.GUID)

    def inBox(self, box, test_mode=True):
        return rs.IsObjectInBox(self.GUID, box, test_mode)
    
    def inGroup(self, group_name=None):
        return rs.IsObjectInGroup(self.GUID, group_name)

    def isHidden(self):
        return rs.IsObjectHidden(self.GUID)

    def isLayout(self):
        return rs.IsLayoutObject(self.GUID)

    def isLocked(self):
        return rs.IsObjectLocked(self.GUID)

    def isNormal(self):
        return rs.IsObjectNormal(self.GUID)

    def isReference(self):
        return rs.IsObjectReference(self.GUID)

    def isSelectable(self):
        return rs.IsObjectSeletable(self.GUID)
        
    def isSelected(self):
        return rs.IsObjectSeleted(self.GUID)
        
    def isSolid(self):
        return rs.IsObjectSolid(self.GUID)
        
    def isValid(self):
        return rs.IsObjectValid(self.GUID)

    def layer(self, layer=None):
        return rs.ObjectLayer(self.GUID, layer)
        
    def layout(self, layout=None, return_name=True):
        return rs.ObjectLayout(self.GUID, layout, return_name)
        
    def linetype(self, linetype=None):
        return rs.ObjectLinetype(self.GUID, linetype)
        
    def linetypeSource(self, source=None):
        return rs.ObjectLinetypeSource(self.GUID, source)

    def lock(self):
        return rs.LockObject(self.GUID)
    
    def MatchObjectAttributes(self, source=None):
        return rs.MatchObjectAttributes(self.GUID, source)

    def mirror(self, start_point, end_point, copy=False):
        return rs.MirrorObject(self.GUID, start_point, end_point, copy)
        
    def move(self, translation):
        self.GUID = rs.MoveObject(self.GUID, translation)
        
    def materialIndex(self):
        return rs.ObjectMaterialIndex(self.GUID)
        
    def materialSource(self, source=None):
        return rs.ObjectMaterialSource(self.GUID, source)
        
    def name(self, name=None):
        return rs.ObjectName(self.GUID, name)
    
    def orient(self, reference, target, flags=0):
        return rs.OrientObject(self.GUID, reference, target, flags)

    def printColor(self, color=None):
        return rs.ObjectPrintColor(self.GUID, color)
        
    def printColorSource(self, source=None):
        return rs.ObjectPrintColorSource(self.GUID, source)
        
    def printWidth(self, width=None):
        return rs.ObjectPrintWidth(self.GUID, width)

    def printWidthSource(self, source=None):
        return rs.ObjectPrintWidthSource(self.GUID, source)
    
    def rotate(self, center_point, rotation_angle, axis=None, copy=False):
        return rs.RotateObject(self.GUID, center_point, rotation_angle, axis, copy)
        
    def scale(self, origin, scale, copy=False):
        return rs.ScaleObject(self.GUID, origin, scale, copy)
        
    def select(self):
        return rs.SelectObject(self.GUID)
        
    def show(self):
        return rs.ShowObject(self.GUID)
    
    def type(self):
        return rs.ObjectType(self.GUID)
           
    def transform(self, matrix, copy=False):
        return rs.TransformObject(self.GUID, matrix, copy)
        
    def unlock(self):
        return rs.UnlockObject(self.GUID)
        
    def unselect(self):
        return rs.UnselectObject(self.GUID)
        