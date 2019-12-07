PATH = "C:\\NAS"
OUTFILE = "data.json"

FILEFORMAT = ["avi", "mp3", "mp4", "mov", "mkv", "ogm"]

CLEAN_PASSONE = "_\[.*?\]|\[.*?\]|\[.*?\]_|_\(.*?\)|\(.*?\)|\{.*?\}|dvdrip.+|xvid.+|divx.+|bluray.+|brrip.+"
CLEAN_PASSTWO = "^ |__+|  +| *$"
CLEAN_PASSTHREE = "^_|_$|\.+$"

CLEAN_REPLACE = "\.| "