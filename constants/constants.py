PATH = "C:\\NAS"
OUTFILE = "data.json"

FILEFORMAT = ["avi", "mp3", "mp4", "mov", "mkv", "jpg", "ogm", "srt"]

CLEAN_PASSONE = r"_\[.*?\]|\[.*?\]|_\(.*?\)|\(.*?\)|.DVDRip|{.*?}|divx.+|bluray.+|brrip.+|dvdrip.+|xvid"
CLEAN_PASSTWO = r"^ |__+|  +"
CLEAN_PASSTHREE = r" "