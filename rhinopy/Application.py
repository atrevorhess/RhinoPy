import rhinoscriptsyntax as rs

#Does this need to be a class?
#Could be a collection of functions
class Application:
    def __init__(self):
        pass

    def addAlias(self, alias, macro):
        return rs.AddAlias(alias, macro)        
    
    def addSearchPath(self, folder, index=-1):
        return rs.AddSearchPath(folder, index)
    
    def aliasCount(self):
        return rs.AliasCount()
    
    def aliasMacro(self, alias, macro=None):
        rs.AliasMacro(alias, macro)
    
    def aliasNames(self):
        return rs.AliasNames()
    
    def appearanceColor(self, item, color=None):
        return rs.AppearanceColor(item, color)  
    
    def AutosaveFile(self):
        pass
    
    def AutosaveInterval(self):
        pass
    
    def BuildDate(self):
        pass
    
    def ClearCommandHistory(self):
        pass
    
    def Command(self):
        pass
    
    def CommandHistory(self):
        pass
    
    def DefaultRenderer(self):
        pass
    
    def DeleteAlias(self):
        pass
    
    def DeleteSearchPath(self):
        pass
    
    def DisplayOleAlerts(self):
        pass
    
    def EdgeAnalysisColor(self):
        pass
    
    def EdgeAnalysisMode(self):
        pass
    
    def EnableAutosave(self):
        pass
    
    def ExeFolder(self):
        pass
    
    def Exit(self):
        pass
    
    def FindFile(self):
        pass
    
    def GetPlugInObject(self):
        pass
    
    def InCommand(self):
        pass
    
    def InstallFolder(self):
        pass
    
    def IsAlias(self):
        pass
    
    def IsCommand(self):
        pass
    
    def IsRunningOnWindows(self):
        pass
    
    def LastCommandName(self):
        pass
        
    def LastCommandResult(self):
        pass

    def LocaleID(self):
        pass
    
    def Ortho(self):
        pass

    def Osnap(self):
        pass

    def OsnapDialog(self):
        pass

    def OsnapMode(self):
        pass

    def Planar(self):
    
        pass
    def PlugIns(self):
    
        pass
    def ProjectOsnaps(self):
        pass
    
    def Prompt(self):
        pass
    
    def RegistryKey(self):
        pass
    
    def ScreenSize(self):
        pass
    
    def SdkVersion(self):
        pass
    
    def SearchPathCount(self):
        pass
    
    def SearchPathList(self):
        pass
    
    def SendKeystrokes(self):
        pass
    
    def Snap(self):
        pass
    
    def StatusBarDistance(self):
        pass
    
    def StatusBarMessage(self):
        pass
    
    def StatusBarPoint(self):
        pass
    
    def StatusBarProgressMeter(self):
        pass
    
    def TemplateFile(self):
        pass
    
    def TemplateFolder(self):
        pass
    
    def WindowHandle(self):
        pass
    
    def WorkingFolder(self):
        pass