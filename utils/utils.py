import os, json

def toFile(inPath, dataDump, outFile="data"):
    with open(os.path.join(inPath, "{}.json".format(outFile)), "w") as jDump2File:
        json.dump(dataDump, jDump2File)

def getFileExtension(inputText):
    return inputText.split(".")[-1]

def extractValues(obj, valueArr, key):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                extractValues(v, valueArr, key)
            elif k == key:
                valueArr.append(v)
    elif isinstance(obj, list):
        for item in obj:
            extractValues(item, valueArr, key)
    return valueArr

def changeValues(obj, key):
    if isinstance(obj, dict):
        for dictKey, dictVal in obj.items():
            if isinstance(dictVal, (dict, list)):
                changeValues(dictVal, key)
            elif dictKey == key:
                #print(dictKey, dictVal)
                obj[dictKey] = dictVal + "_TEST"
                print(obj)

    elif isinstance(obj, list):
        for item in obj:
            changeValues(item, key)

