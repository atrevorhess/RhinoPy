class :
    def __init__(self):
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

    def description(self, description=None):
        return rs.BlockDescription(self.name)

    def instanceCount(self, encapsulation_level=0):
        return rs.BlockInstanceCount(self.name, encapsulation_level)

    def insertPoint(self):
        pass

    def InstanceName(self):
        pass

    def Instances(self):
        pass

    def InstanceXform(self):
        pass

    def Names(self):
        pass

    def ObjectCount(self):
        pass

    def Objects(self):
        pass

    def Path(self):
        pass

    def Delete(self):
        pass

    def ExplodeInstance(self):
        pass

    def Insert(self):
        pass

    def Is(self):
        pass

    def IsEmbedded(self):
        pass

    def IsInstance(self):
        pass

    def IsInUse(self):
        pass

    def IsReference(self):
        pass

    def Rename(self):
        pass
