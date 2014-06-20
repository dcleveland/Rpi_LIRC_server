"""Web app to operate an IR blaster on a RaspberryPi running lirc.

"""

from subprocess import PIPE
from subprocess import Popen

from flask import Flask, request, session, g, redirect, url_for, abort, \
  render_template, flash
import remotes as conf

app = Flask(__name__)

@app.route("/hold/r=<remote>&c=<command>")
def holdCode(remote, command):
  assert remote in conf.REMOTES, "Remote %s is not valid." % remote
  assert command in conf.REMOTES[remote], "Command %s not found" % code
  assert conf.REMOTES[remote][command]["repeat"]
  com = "irsend SEND_START %s %s" % (remote, command)
  Popen(com, stdout=PIPE, shell=True)
  return "Holding %s command %s." % (remote, command)

@app.route("/release/r=<remote>&c=<command>")
def releaseCode(remote, command):
  assert remote in conf.REMOTES, "Remote %s is not valid." % remote
  assert command in conf.REMOTES[remote], "Command %s not found" % code
  assert conf.REMOTES[remote][command]["repeat"]
  com = "irsend SEND_STOP %s %s" % (remote, command)
  Popen(com, stdout=PIPE, shell=True)
  return "Releasing %s command %s." % (remote, command)  

@app.route("/blast/r=<remote>&c=<command>&n=<count>")
def sendCode(remote, command, count):
  assert remote in conf.REMOTES, "Remote %s is not valid." % remote
  assert command in conf.REMOTES[remote], "Command %s not found" % code
  com = "irsend SEND_ONCE --count=%s %s %s" % (count, remote, command)
  Popen(com, stdout=PIPE, shell=True)
  return "Sending %s Command %s %s times" % (remote, command, count)

@app.route("/macro/id=<macro_id>")
def sendMacro(macro_id):
  assert macro_id in conf.MACROS, "Macro not found."
  coms = conf.MACROS[macro_id]["commands"]
  sleep_time = conf.MACROS[macro_id]["sleep"]
  base = "irsend SEND_ONCE %s %s; sleep %s"
  macro = ";".join([base % (x[0], x[1], sleep_time) for x in coms])
  Popen(macro, stdout=PIPE, shell=True)

@app.route("/")
def index():
  return render_template('index.html', remotes=conf.REMOTES, macros=conf.MACROS)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
  #app.run()