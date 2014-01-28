import rhinoscriptsyntax as rs

class Group:
    def __init__(self, name):
        self.name = name if self._isGroup(name) else self._add(name) 

    def _add(self, group_name=None):
        return rs.AddGroup(group_name)

    def _isGroup(self, name):
        #Implemented for constructor so that 
        return rs.IsGroup(name)
    
    def addObject(self, objects):
        #add one or multiple objects into the group

    
    def delete(self):
        # del self
        return rs.DeleteGroup(self.name)
    
    #Needs to be a document Method
    def GroupCount(self):
        pass
    
    #Needs to be a document Method
    def GroupNames(self):
        pass
    
    def hide(self):
        return rs.HideGroup(self.name)
    
    def isEmpty(self):
        return rs.IsGroupEmpty(self.name)
    
    def lock(self):
        return rs.LockGroup(self.name)
    
    # Needs to be a document Method
    # def RemoveObjectFromAllGroups(self):
    #     pass
    
    def removeObjectFromGroup(self, objects):
        #remove one or multiple objects into the group

    # def RemoveObjectsFromGroup(self):
    #     pass
    
    def rename(self, new_name=None):
        return self.RenameGroup(self.name, new_name)
    
    def show(self):
        return rs.ShowGroup(self.name)
    
    def unlock(self):
        return rs.UnlockGroup(self.name)