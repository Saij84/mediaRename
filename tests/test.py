from mediaRename.constants import constants as CONST
from mediaRename.core import tree2Json as t2j
from pprint import pprint
import json, re
from mediaRename.utils import utils

jsonFilePath = "\\".join([CONST.PATH, CONST.OUTFILE])
cleanStart = re.compile(CONST.RE_REPLACE)
arr = list()

with open(jsonFilePath) as json_file:
    data = json.load(json_file)
    # extractData = utils.extractValues(data, arr, "newName")
    # pprint(extractData)
    utils.changeValues(data, "newName")
    utils.toFile(inPath=CONST.PATH, dataDump=data)
    pprint(data)
