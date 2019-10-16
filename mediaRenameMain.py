from pprint import pprint
from mediaRename.core import tree2Json
from mediaRename.utils import utils

path = r"C:\NAS\Anime\Avatar"
t2j = tree2Json.Tree2json()

data = t2j.tree2json(path)
pprint(data)
utils.toFile(inPath=path, dataDump=data)
