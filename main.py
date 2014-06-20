"""Web app to operate an IR blaster on a RaspberryPi running lirc.

"""
from subprocess import PIPE
from subprocess import Popen

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
  return render_template('index.html')


@app.route("/blast?r=<remote>&c=<command>&n=<count>")
def sendCode(remote, command, count):
  assert remote in conf.REMOTES, "Remote %s is not valid." % remote
  assert command in conf.REMOTES[remote], "Command %s not found" % code
  code = conf.REMOTES[remote][command]["code"]
  com = "irsend --count=%s %s %s" % (count, remote, code)
  Popen(com, stdout=PIPE, shell=True)