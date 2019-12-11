import re
from mediaRename.constants import constants as CONST


def cleanReplace(data):
    """
    Takes each dict object and clean
    :param data: dict object
    :return: none
    """
    dataIn = data["files"]

    # (regX, replaceSTR)
    cleanPasses = [(CONST.CLEAN_PASSONE, ""), (CONST.CLEAN_PASSTWO, ""),
                   (CONST.CLEAN_PASSTHREE, ""), (CONST.CLEAN_REPLACE, "_")]

    for cPass, replaceSTR in cleanPasses:
        seachString = re.compile(cPass, re.IGNORECASE)

        for fileDict in dataIn:
            if isinstance(fileDict, dict):
                changedVal = seachString.sub(replaceSTR, fileDict["newName"])
                fileDict["newName"] = changedVal
