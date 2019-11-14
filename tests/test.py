from pprint import pprint
import os
from mediaRename.core import tree2Json
from mediaRename.utils import utils
from mediaRename.core.output import Output as out
from mediaRename.core.clean import clean
from mediaRename.constants import constants as CONST

t2j = tree2Json.Tree2json()
data = t2j.tree2json(CONST.PATH)
jsonNodes = data.get("files")

clean(data, "newName", cleanPass="cleanPassOne")
# cln.clean(data, "newName", cleanPass="cleanPassTwo")

for node in jsonNodes:
    returnPath = utils.returnPaths(node)
    print(returnPath.oldPath)
    print(returnPath.newPath)

out.toFile(outPath=CONST.PATH, jsonDataDump=data)
