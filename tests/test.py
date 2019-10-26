from mediaRename.constants import constants as CONST
from pprint import pprint
import json, re, os
from mediaRename.utils import utils
from mediaRename.core import cleaning

path = "\\".join([CONST.PATH, CONST.OUTFILE])
cleaning.clean(path, "cleanPassOne")
