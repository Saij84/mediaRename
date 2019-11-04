from mediaRename.constants import constants as CONST
from pprint import pprint
import json, re, os
from mediaRename.utils import utils

path = os.path.join(CONST.PATH, CONST.OUTFILE)

# with open(path) as json_file:
#     data = json.load(json_file)
#     localData = utils.reconstrucPath(data, key="")
#     pprint(localData)

print(help(json))