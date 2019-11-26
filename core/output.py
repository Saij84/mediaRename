import json
import os


def toFile(outPath, jsonDataDump):
    with open(os.path.join(outPath, "data.json"), "w") as jDump2File:
        json.dump(jsonDataDump, jDump2File)

src = r"C:\NAS\Anime\Code Geass - Lelouch of the Rebellion R2\[Chihiro]Code_Geass_Lelouch_of_the_Rebellion_R2_08_[h264][52327873].mkv"
trg = r"C:\NAS\Anime\Code Geass - Lelouch of the Rebellion R2\[Chihiro]Code_Geass_Lelouch_of_the_Rebellion.mkv"

def renameFiles(srcPath, trgPath):
    os.rename(srcPath, trgPath)

# renameFiles(src, trg)
# renameFiles(trg, src)