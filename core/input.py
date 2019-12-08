import os
from mediaRename.constants import constants as CONST
from mediaRename.utils import utils


class Tree2Data:
    def __init__(self):
        self.returnDict = {'files': []}

    def tree2Data(self, inPath):
        """
        Takes a root path, traverse the folder tree and store the data in json form
        :param inPath: path i.e. 'c:\\Foo'
        :return: dict
        """
        if os.path.isdir(inPath):
            for x in os.listdir(inPath):
                self.tree2Data(os.path.join(inPath, x))
        else:
            filename = utils.seperateFileExtension(os.path.basename(inPath))
            if filename.extension in CONST.FILEFORMAT:
                self.returnDict['files'].append({
                    'oldName': os.path.basename(inPath),
                    'newName': filename.noExtension,
                    'extension': filename.extension,
                    'path': "\\".join(inPath.split("\\")[:-1])}
                )
        return self.returnDict
