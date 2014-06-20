"""lirc_parser.py

Script to parse LIRC remote config files.

Input: LIRC Filename(s) or URL(s)
Output: Python file (remotes.py) containing a dict of remotes

"""

import codecs
from collections import defaultdict
import re

REMOTE_START = "begin remote"
REMOTE_END = "end remote"
CODES_START = "begin codes"
CODES_END = "end codes"

def loadFile(fn):
  try:
    fh = codecs.open(fn, "r")
    return fh
  except:
    return False

def getUrl(url):
  com = """curl "%s" 2>/dev/null > remote.txt"""
  Popen(com % url, stdout=PIPE, shell=True).wait()
  try:
    fh = codecs.open("remote.txt", "r")
    return fh
  except:
    return False

def parseFile(fh):
  this_remote = defaultdict()
  name = ""
  begin = False
  while True:
    try:
      l = fh.next().replace("\r", "").replace("\n", "")
    except:
      break
    if re.search("name\b?(.*)", l.strip()):
      name = re.search("name\b?(.*)", l.strip()).groups()[0].strip()
      print "found a name"
    if re.search(CODES_START, l.strip()):
      begin = True
    elif name and begin:
      code = [x for x in l.split(" ") if x]
      if len(code) == 2:
        clean = code[0].lower().replace("_", " ").title()
        this_remote[code[0]] = {"show": 1, "repeat": 0, "display": clean}
    if re.search(CODES_END, l.strip()):
      break
  return this_remote








