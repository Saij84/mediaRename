from pprint import pprint
import time

from mediaRename.core import tree2Json
from mediaRename.utils import utils
from mediaRename.core import output as out
from mediaRename.core import clean as cln
from mediaRename.constants import constants as CONST

t2j = tree2Json.Tree2json()
data = t2j.tree2json(CONST.PATH)
jsonNodes = data.get("files")

average = 0
repeats = 100
for i in range(repeats):
    timeStart = time.time()
    cln.cleanReplace(data, cleanPass="cleanPassOne", replaceSTR="")
    cln.cleanReplace(data, cleanPass="cleanPassTwo", replaceSTR="")
    cln.cleanReplace(data, cleanPass="cleanPassThree", replaceSTR="")
    timeEnd = time.time()

    timeResult = timeEnd-timeStart
    average += timeResult
    print(timeResult)
print("average:", average/repeats)

# cln.cleanReplace(data, cleanPass="cleanPassFinal", replaceSTR="_")
# for node in jsonNodes:
#     returnPath = utils.returnPaths(node)
#     print(returnPath.oldPath)
#     print(returnPath.newPath)
# out.toFile(outPath=CONST.PATH, jsonDataDump=data)
