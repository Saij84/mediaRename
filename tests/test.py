from mediaRename.constants import constants as CONST
from pprint import pprint
import json, re, os
from mediaRename.utils import utils

path = "\\".join([CONST.PATH, CONST.OUTFILE])

with open(path) as json_file:
    data = json.load(json_file)

    utils.clean(data, "newName", cleanPass="cleanPassOne")
    utils.toFile(outPath=CONST.PATH, jsonDataDump=data)
    pprint(data)