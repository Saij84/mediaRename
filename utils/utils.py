import collections as coll
import os


def seperateFileExtension(inputText):
    """
    seperates file extension from the name
    :param inputText: str
    :return: named tuples
    """
    separatedNames = coll.namedtuple("separatedNames", ["noExtension", "extension"])
    noExtensionName = ".".join(inputText.split(".")[:-1])
    fileExtension = inputText.split(".")[-1]
    name = separatedNames(noExtensionName, fileExtension)
    return name


def returnPaths(jsonObj):
    """
    takes a json dict and returns new and old paths
    :param jsonObj: json dict
    :return: tuple of paths (oldPath, newPath)
    """
    assert isinstance(jsonObj, dict), "In object not a dict"

    paths = coll.namedtuple("paths", ["oldPath", "newPath"])
    oldName = jsonObj.get("oldName")
    newName = jsonObj.get("newName")
    extension = jsonObj.get("extension")
    path = jsonObj.get("path")

    paths = paths(os.path.join(path, oldName),
                  os.path.join(path, newName) + "." + extension)
    return paths
