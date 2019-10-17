import os, json

def toFile(inPath, dataDump, outFile="data"):
    with open(os.path.join(inPath, "{}.json".format(outFile)), "w") as jDump2File:
        json.dump(dataDump, jDump2File)

def getFileExtension(inputText):
    return inputText.split(".")[-1]
