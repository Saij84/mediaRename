import os, json, re
from mediaRename.constants import constants as CONST

def toFile(outPath, jsonDataDump):
    with open(os.path.join(outPath, "data.json"), "w") as jDump2File:
        json.dump(jsonDataDump, jDump2File)

def seperateFileExtension(inputText):
    noExtensionName = inputText.split(".")[0]
    fileExtension = inputText.split(".")[-1]
    return noExtensionName, fileExtension

def extractValues(data, key, valueArr):
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                extractValues(v, key, valueArr)
            elif k == key:
                valueArr.append(v)
    elif isinstance(data, list):
        for item in data:
            extractValues(item, key, valueArr)
    return valueArr

def cleanNewName(data, key, cleanPass):
    cleanPassDict = {"cleanPassOne": CONST.CLEAN_PASSONE, "cleanPassTwo": CONST.CLEAN_PASSTWO,
                     "cleanPassThree": CONST.CLEAN_PASSTHREE}
    print(cleanPass)
    seachString = re.compile(cleanPassDict[cleanPass])
    if isinstance(data, dict):
        for dictKey, dictVal in data.items():
            if isinstance(dictVal, (dict, list)):
                cleanNewName(dictVal, key, cleanPass)
            elif dictKey == key:
                changedVal = seachString.sub("", dictVal)
                data[dictKey] = changedVal

    elif isinstance(data, list):
        for item in data:
            cleanNewName(item, key, cleanPass)

