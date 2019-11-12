import os, collections
from mediaRename.constants import constants as CONST
from mediaRename.utils import utils

class Tree2json:
    def __init__(self):
        self.returnDict = {'files': []}

    def tree2json(self, inPath):
        if os.path.isdir(inPath):
            for x in os.listdir(inPath):
                self.tree2json(os.path.join(inPath, x))
        else:
            filename = utils.seperateFileExtension(os.path.basename(inPath))
            if filename.extension in CONST.FILEFORMAT:
                self.returnDict['files'].append({
                    'oldName': os.path.basename(inPath),
                    'newName': filename.noExtension,
                    'type': filename.extension,
                    'path': "\\".join(inPath.split("\\")[:-1])}
                )
        return self.returnDict
