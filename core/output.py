import json
import os
from mediaRename.constants import constants as CONST

def toFile(jsonDataDump):
    """
    Write to json file
    :param jsonDataDump: jason data
    :return: None
    """
    with open(os.path.join(CONST.INPATH, CONST.OUTFILE), "w") as jDump2File:
        json.dump(jsonDataDump, jDump2File)

def renameFiles(srcPath, trgPath):
    """
    Rename files
    :param srcPath: path
    :param trgPath: path
    :return: None
    """
    os.rename(srcPath, trgPath)
