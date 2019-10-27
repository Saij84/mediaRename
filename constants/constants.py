PATH = "C:\\NAS\\Anime"
OUTFILE = "data.json"

FILEFORMAT = ["avi", "mp3", "mp4", "mov", "mkv", "jpg", "ogm", "srt"]

CLEAN_PASSONE = r"_\[.*?\]|\[.*?\]|_\(.*?\)|\(.*?\)|.DVDRip|{.*?}|XviD.+|divx.+/i"
CLEAN_PASSTWO = r"^ |__+|  +"
CLEAN_PASSTHREE = r" "