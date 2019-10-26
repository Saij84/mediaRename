from mediaRename.constants import constants as CONST
from mediaRename.utils import utils
from pprint import pprint
import json

def clean(jsonFilePath, cleanPass):
    with open(jsonFilePath) as json_file:
        data = json.load(json_file)

        utils.cleanNewName(data, "newName", cleanPass=cleanPass)
        utils.toFile(outPath=CONST.PATH, jsonDataDump=data)
        pprint(data)
