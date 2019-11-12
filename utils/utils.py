import os, json, re
import collections as coll
from mediaRename.constants import constants as CONST

def toFile(outPath, jsonDataDump):
    with open(os.path.join(outPath, "data.json"), "w") as jDump2File:
        json.dump(jsonDataDump, jDump2File)

def seperateFileExtension(inputText):
    seperatedNames = coll.namedtuple("seperatedNames", ["noExtension", "extension"])
    noExtensionName = ".".join(inputText.split(".")[:-1])
    fileExtension = inputText.split(".")[-1]
    name = seperatedNames(noExtensionName, fileExtension)
    return name

def clean(data, key, cleanPass):
    cleanPassDict = {"cleanPassOne": CONST.CLEAN_PASSONE, "cleanPassTwo": CONST.CLEAN_PASSTWO,
                     "cleanPassThree": CONST.CLEAN_PASSTHREE}

    seachString = re.compile(cleanPassDict[cleanPass], re.IGNORECASE)
    if isinstance(data, dict):
        for dictKey, dictVal in data.items():
            if isinstance(dictVal, (dict, list)):
                clean(dictVal, key, cleanPass)
            elif dictKey == key:
                changedVal = seachString.sub("", dictVal)
                data[dictKey] = changedVal
    elif isinstance(data, list):
        for item in data:
            clean(item, key, cleanPass)
