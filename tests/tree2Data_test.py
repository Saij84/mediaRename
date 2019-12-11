import os
import shutil
import unittest
import re
from mediaRename.constants import constants as CONST
from mediaRename.core.input import Tree2Data as t2d
from mediaRename.utils import utils


def cleanReplace(data):
    """
    Takes each dict object and clean
    :param data: dict object
    :return: none
    """
    dataIn = data["files"]

    # (regX, replaceSTR)
    cleanPasses = [(CONST.CLEAN_PASSONE, ""), (CONST.CLEAN_PASSTWO, ""),
                   (CONST.CLEAN_PASSTHREE, ""), (CONST.CLEAN_REPLACE, "_")]

    for cPass, replaceSTR in cleanPasses:
        seachString = re.compile(cPass, re.IGNORECASE)

        for fileDict in dataIn:
            if isinstance(fileDict, dict):
                changedVal = seachString.sub(replaceSTR, fileDict["newName"])
                fileDict["newName"] = changedVal
    return dataIn

class TestTree2Data(unittest.TestCase):

    def setUp(self):
        self.tree2data = t2d()
        self.rootPath = "C:\\testCase"
        self.folders = ["mainFloder1", "mainFloder2", "mainFloder3"]
        self.subFolders = ["subfolder1", "subfolder2"]
        self.files = ["test.file[2010]_movie1.avi", "test_file[2010] movie2.mkv"]
        self.dummyPath = "C:\\testCase\\mainFloder1\\subfolder2\\test_file[2010]_movie5.avi"
        self.renamedFiles = ["test_file_movie1.avi", "test_file_movie2.mkv"]

        for folder in self.folders:
            for subfolder in self.subFolders:
                folderPath = os.path.join(self.rootPath, folder, subfolder)
                os.makedirs(folderPath, exist_ok=True)

                for file in self.files:
                    filePath = os.path.join(folderPath, file)
                    file = open(filePath, "w")
                    file.close()

        self.data = self.tree2data.tree2Data(self.rootPath)

    def test_tree2Data(self):
        for dictObj in self.data["files"]:
            path = utils.returnPaths(dictObj)
            self.assertEqual(os.path.isfile(path.oldPath), True, "{} Path does not exists".format(path))
            self.assertFalse(os.path.isfile(self.dummyPath))

    def test_cleanReplace(self):
        cleanData = cleanReplace(self.data)

        for dataNode in cleanData:
            self.assertTrue(".".join([dataNode["newName"], dataNode["extension"]]) in self.renamedFiles)

    def tearDown(self):
        if self.rootPath:
            shutil.rmtree(self.rootPath, ignore_errors=True)
