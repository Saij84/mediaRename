from pprint import pprint
from mediaRename.core import tree2Json
from mediaRename.utils import utils
from mediaRename.constants import constants as CONST

t2j = tree2Json.Tree2json()
data = t2j.tree2json(CONST.PATH)
pprint(data)
utils.toFile(inPath=CONST.PATH, dataDump=data)
