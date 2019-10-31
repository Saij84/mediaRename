PATH = "C:\\NAS"
OUTFILE = "data.json"

FILEFORMAT = ["avi", "mp3", "mp4", "mov", "mkv", "jpg", "ogm", "srt"]

CLEAN_PASSONE = "_\[.*?\]|\[.*?\]|_\(.*?\)|\(.*?\)|{.*?}"
CLEAN_PASSTWO = "dvdrip.+|xvid.+|divx.+|bluray.+|brrip.+"
CLEAN_PASSTHREE = r"^ |__+|  +"