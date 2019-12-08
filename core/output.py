import json
import os


def toFile(outPath, jsonDataDump):
    """
    Write to json file
    :param outPath: path
    :param jsonDataDump: data
    :return: None
    """
    with open(os.path.join(outPath, "data.json"), "w") as jDump2File:
        json.dump(jsonDataDump, jDump2File)

def renameFiles(srcPath, trgPath):
    """
    Rename files
    :param srcPath: path
    :param trgPath: path
    :return: None
    """
    os.rename(srcPath, trgPath)
