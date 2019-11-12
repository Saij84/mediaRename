from mediaRename.core import tree2Json
from mediaRename.utils import utils
from mediaRename.constants import constants as CONST

t2j = tree2Json.Tree2json()
data = t2j.tree2json(CONST.PATH)
utils.clean(data, "newName", cleanPass="cleanPassOne")
utils.clean(data, "newName", cleanPass="cleanPassTwo")
utils.clean(data, "newName", cleanPass="cleanPassThree")
utils.toFile(outPath=CONST.PATH, jsonDataDump=data)
