import os, json, re
from pprint import pprint

reString = re.compile(r"\[.*?\]")
inPath = "C:\\NAS\\Anime"
outFile = os.path.basename(inPath)

def tree2json(path):
    returnDict = {'oldName': os.path.basename(path)}

    if os.path.isdir(path):
        returnDict['type'] = "directory"
        returnDict['children'] = [tree2json(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        fileExtension = returnDict.get("oldName", "").split(".")[-1]
        newName = reString.sub("", os.path.basename(path))
        returnDict['newName'] = newName
        returnDict['type'] = fileExtension
    return returnDict
jDump = tree2json(inPath)
pprint(jDump)

# with open(os.path.join(inPath, "{}.json".format(outFile)), "w") as jDump2File:
#     json.dump(jDump, jDump2File)
