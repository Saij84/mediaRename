import re
from mediaRename.constants import constants as CONST


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
