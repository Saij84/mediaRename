import os, re
from mediaRename.constants import constants as CONST
from mediaRename.utils import utils

class Tree2json:
    def tree2json(self, inPath):
        returnDict = {'oldName': os.path.basename(inPath)}
        if os.path.isdir(inPath):
            returnDict['type'] = "directory"
            returnDict['children'] = [self.tree2json(os.path.join(inPath, x)) for x in os.listdir(inPath)]
        else:
            seperatedNames = utils.seperateFileExtension(returnDict.get("oldName", ""))
            print(seperatedNames)
            if seperatedNames[1] in CONST.FILEFORMAT:
                returnDict['newName'] = seperatedNames[0]
                returnDict['type'] = seperatedNames[1]
        return returnDict
