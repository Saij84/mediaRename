import json
import os


class Output:
    def toFile(self, outPath, jsonDataDump):
        with open(os.path.join(outPath, "data.json"), "w") as jDump2File:
            json.dump(jsonDataDump, jDump2File)
