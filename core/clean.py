import re
from mediaRename.constants import constants as CONST


def cleanReplace(data, cleanPass, replaceSTR=""):
    """

    :param data:
    :param cleanPass:
    :param replaceSTR:
    :return: none
    """
    dataIn = data["files"]
    cleanPassDict = {"cleanPassOne": CONST.CLEAN_PASSONE, "cleanPassTwo": CONST.CLEAN_PASSTWO,
                     "cleanPassThree": CONST.CLEAN_PASSTHREE, "cleanPassFinal": CONST.CLEAN_REPLACE}
    seachString = re.compile(cleanPassDict[cleanPass], re.IGNORECASE)

    for fileDict in dataIn:
        if isinstance(fileDict, dict):
            changedVal = seachString.sub(replaceSTR, fileDict["newName"])
            fileDict["newName"] = changedVal
