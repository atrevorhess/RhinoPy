import rhinoscriptsyntax as rs
from Point import Point
from Transformation import Transformation

class Block:
    def __init__(self, objects, base_point, name, delete_input):
        self.name = self._add(objects, base_point, name, delete_input)
        #Blocks have name, instances have GUIDs
        #Should blocks and instances be split into two different classes??

    def _add(self, objects, base_point, name=None, delete_input=False):
        return rs.AddBlock(objects, base_point, name, delete_input)

    def containerCount(self):
        return rs.BlockContainerCount(self.name)

    def containers(self):
        return rs.BlockContainers(self.name)

    #Document Method
    # def Count(self):
    #     pass
    # def Names(self):
    #     pass

    def description(self, description=None):
        return rs.BlockDescription(self.name)

    def instanceCount(self, encapsulation_level=0):
        return rs.BlockInstanceCount(self.name, encapsulation_level)

    def instances(self):
        return rs.BlockInstances(self.name)

    def objectCount(self):
        return rs.BlockObjectCount(self.name)

    def objects(self):
        return rs.BlockObjects(self.name)

    def path(self):
        return rs.BlockPath(self.name)

    def delete(self):
        return rs.DeleteBlock(self.name)
        #If true delete self

    def Insert(self, insertion_point, scale=[1, 1, 1], angle=0, rotation_normal=[0, 0, 1]):
        return Instance(self.name, insertion_point, scale, angle, rotation_normal)

    def isEmbedded(self):
        return rs.IsBlockEmbedded(self.name)

    def isInUse(self, search_space=0):
        return rs.IsBlockInUse(self.name, search_space)

    def isReference(self):
        return rs.IsBlockReference(self.name)

    def rename(self, new_name):
        self.name = rs.RenameBlock(self.name, new_name)
        return self.name

class Instance(Block):
    def __init__(self, block_name, insertion_point, scale=[1, 1, 1], angle=0, rotation_normal=[0, 0, 1]):
        self.GUID = self._add(block_name, insertion_point, scale, angle, rotation_normal)

    def _add(self, block_name, insertion_point, scale=[1, 1, 1], angle=0, rotation_normal=[0, 0, 1]):
        return rs.InsertBlock(block_name, insertion_point, scale, angle, rotation_normal)

    def _isInstance(self):
        pass

    def explode(self):
        return rs.ExplodeBlockInstance(self.GUID)

    def insertPoint(self):
        return Point(rs.BlockInstanceInsertPoint(self.name))

    def name(self, guid):
        return rs.BlockInstanceName(guid)

    def xform(self):
        return [Transformation(item) for item in rs.BlockInstanceXForm(self.GUID)]