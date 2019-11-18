import re
from mediaRename.constants import constants as CONST
from pprint import pprint


def cleanReplace(data, cleanPass, replaceSTR):
    cleanPassDict = {"cleanPassOne": CONST.CLEAN_PASSONE, "cleanPassTwo": CONST.CLEAN_PASSTWO,
                     "cleanPassThree": CONST.CLEAN_PASSTHREE, "cleanPassFinal": CONST.CLEAN_REPLACE}

    seachString = re.compile(cleanPassDict[cleanPass], re.IGNORECASE)
    if isinstance(data, dict):
        for dictKey, dictVal in data.items():
            if isinstance(dictVal, (dict, list)):
                cleanReplace(dictVal, cleanPass, replaceSTR)
            elif dictKey == "newName":
                changedVal = seachString.sub(replaceSTR, dictVal)
                data[dictKey] = changedVal
    elif isinstance(data, list):
        for item in data:
            cleanReplace(item, cleanPass, replaceSTR)

def cleanReplacev2(data, cleanPass, replaceSTR):
    dataIn = data["files"]
    cleanPassDict = {"cleanPassOne": CONST.CLEAN_PASSONE, "cleanPassTwo": CONST.CLEAN_PASSTWO,
                     "cleanPassThree": CONST.CLEAN_PASSTHREE, "cleanPassFinal": CONST.CLEAN_REPLACE}
    seachString = re.compile(cleanPassDict[cleanPass], re.IGNORECASE)

    for fileDict in dataIn:
        if isinstance(fileDict, dict):
            changedVal = seachString.sub(replaceSTR, fileDict["newName"])
            fileDict["newName"] = changedVal
