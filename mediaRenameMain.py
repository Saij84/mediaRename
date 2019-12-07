import os
from mediaRename.core import input
from mediaRename.core import output as out
from mediaRename.utils import utils
from mediaRename.core import clean as cln
from mediaRename.constants import constants as CONST
import json

t2j = input.Tree2Data()
data = t2j.tree2Data(CONST.PATH)
jsonNodes = data.get("files")

cln.cleanReplace(data, cleanPass="cleanPassOne")
cln.cleanReplace(data, cleanPass="cleanPassTwo")
cln.cleanReplace(data, cleanPass="cleanPassThree")
cln.cleanReplace(data, cleanPass="cleanPassFinal", replaceSTR="_")

out.toFile(outPath=CONST.PATH, jsonDataDump=data)

with open(os.path.join(CONST.PATH, CONST.OUTFILE), "r") as jsonFile:
    jsonData = json.load(jsonFile)

for i in jsonData.get("files"):
    path = utils.returnPaths(i)
    if os.path.exists(path.newPath):
        pass
    else:
        out.renameFiles(path.oldPath, path.newPath)
