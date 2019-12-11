import os
import shutil
import unittest
import json
from mediaRename.core.input import Tree2Data as t2d
from mediaRename.core import clean
from mediaRename.core import output
from mediaRename.utils import utils

class TestTree2Data(unittest.TestCase):

    def setUp(self):
        self.rootPath = "C:\\testCase"
        self.folders = ["mainFloder1", "mainFloder2", "mainFloder3"]
        self.subFolders = ["subfolder1", "subfolder2"]
        self.files = ["test.file[2010]_movie1.avi", "test_file[2010] movie2.mkv"]
        self.tree2data = t2d()
        self.dummyPath = "C:\\testCase\\mainFloder1\\subfolder2\\test_file[2010]_movie5.avi"

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
        cleanData = clean.cleanReplace(self.data)
        print(cleanData)

        for dataNode in cleanData:
            self.assertTrue(dataNode["newName"] in ["test_file_movie1.avi", "test_file_movie2.mkv"])

    def tearDown(self):
        if self.rootPath:
            shutil.rmtree(self.rootPath, ignore_errors=True)
