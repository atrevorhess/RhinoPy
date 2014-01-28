import rhinoscriptsyntax as rs

class Layer:
    def __init__(self, name=None, color=0, visible=True, locked=False, parent=None):
        self.name = self._add(name, color, visible, locked, parent)


    def _add(self, name, color, visible, locked, parent):
        if not self._isLayer(name):
            return rs.AddLayer(name, color, visible, locked, parent)
        else:
            #Recursive function that increments layer name until it finds a name that is not already in the model
            try:
                current_name, index = name.split('-')
                name = current_name + '-' + (int(index) + 1)
            except:
                name = name + '-' + 1
            self._add(name, color, visible, locked, parent)
            

    def _isLayer(self, name):
        return rs.IsLayer(name)

    def makeCurrent(self):
        return rs.CurrentLayer(self.name)

    def delete(self):
        # del self
        return rs.DeleteLayer(self.name)

    def expand(self, expand_boolean):
        return rs.ExpandLayer(self.name, expand_boolean)

    def isChangeable(self):
        return rs.IsLayerChangeable(self.name)

    def isChildOf(self, test_layer):
        return rs.IsLayerChildOf(self.name, test_layer)

    def isCurrent(self):
        return rs.IsLayerCurrent(self.name)

    def isEmpty(self):
        return rs.IsLayerEmpty(self.name)

    def isExpanded(self):
        return rs.IsLayerExpanded(self.name)

    def isLocked(self):
        return rs.IsLayerLocked(self.name)

    def isOn(self):
        return rs.IsLayerOn(self.name)

    def isParentOf(self, test_layer):
        return rs.IsLayerParentOf(self.name, test_layer)

    def isReference(self):
        return rs.IsLayerReference(self.name)

    def isSelectable(self):
        return rs.IsLayerSelectable(self.name)

    def isVisible(self):
        return rs.IsLayerVisible(self.name)

    def childCount(self):
        return rs.LayerChildCount(self.name)

    def children(self):
        return rs.LayerChildren(self.name)

    def color(self, color=0):
        return rs.LayerColor(self.name, color)

    # Should be a method of the document
    # def LayerCount(self):
    #     pass

    def linetype(self, linetype=None):
        return rs.LayerLinetype(self.name, linetype)

    def locked(self, locked=None):
        return rs.LayerLocked(self.name, locked)

    def materialIndex(self):
        return rs.LayerMaterialIndex(self.name)

    # Should be a method of the document
    # def LayerNames(self):
    #     pass

    def order(self):
        return rs.LayerOrder(self.name)

    def printColor(self, color=None):
        return rs.LayerPrintColor(self.name, color)

    def printWidth(self, width=None):
        return rs.LayerPrintWidth(self.name, width)

    def visible(self, visible=None):
        return rs.LayerVisible(self.name, visible)

    def parent(self, parent=None):
        return rs.ParentLayer(self.name, parent)
