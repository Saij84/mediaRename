import json
import os


def toFile(outPath, jsonDataDump):
    with open(os.path.join(outPath, "data.json"), "w") as jDump2File:
        json.dump(jsonDataDump, jDump2File)

def renameFiles(srcPath, trgPath):
    os.rename(srcPath, trgPath)
