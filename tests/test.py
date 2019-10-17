from mediaRename.utils import utils
from mediaRename.constants import constants as CONST
from mediaRename.core import tree2Json as t2j
from pprint import pprint
import json, re

jsonFilePath = "C:\\NAS\\Anime\\data.json"
cleanStart = re.compile(CONST.RE_REPLACE)

with open(jsonFilePath) as json_file:
    data = json.load(json_file)

    for p in data['newName']:
        pprint(cleanStart.findall(p))
    #     print('Name: ' + p['name'])
    #     print('Website: ' + p['website'])
    #     print('From: ' + p['from'])
    #     print('')