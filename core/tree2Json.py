import os, re
from mediaRename.constants import constants as CONST


class Tree2json:
    def __init__(self):
        self.reString = re.compile((r"\[.*?\]|.DVDRip|{.*?}"))

    def tree2json(self, inPath):
        returnDict = {'oldName': os.path.basename(inPath)}
        if os.path.isdir(inPath):
            returnDict['type'] = "directory"
            returnDict['children'] = [self.tree2json(os.path.join(inPath, x)) for x in os.listdir(inPath)]
        else:
            fileExtension = returnDict.get("oldName", "").split(".")[-1]
            if fileExtension in CONST.FILEFORMAT:
                newName = self.reString.sub("", os.path.basename(inPath))
                returnDict['newName'] = newName
                returnDict['type'] = fileExtension
        return returnDict
