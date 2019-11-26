import json
import os
from pprint import pprint
import re
from mediaRename.constants import constants as CONST

jsonFile = os.path.join(CONST.PATH, CONST.OUTFILE)
with open(jsonFile, 'r') as data:
    datastore = json.load(data)
    # .+_. +$ |
    dataIn = datastore["files"]
    seachString = re.compile("([^ ]+)$", re.IGNORECASE)

    matchCount = 0
    failCount = 0
    for fileDict in dataIn:
        if isinstance(fileDict, dict):
            namePattern = seachString.findall(fileDict["newName"])
            if namePattern == []:
                print(fileDict["newName"])
            # print(namePattern)
            if namePattern:
                if namePattern[0] == fileDict["newName"]:
                    matchCount += 1
                else:
                    failCount += 1
            else:
                failCount += 1

    print("totalNodes:", (matchCount + failCount), failCount/(matchCount + failCount) *100)
