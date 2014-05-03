import datetime

import relativedates

import supybot.ircutils as ircutils
import supybot.utils as utils

class Steamservice:
    def __init__(self, name, key, status, health, time=None):
        self.name = name
        self.key = key
        self.status = status
        self.health = health

        if time:
            self.time = datetime.datetime.fromtimestamp(int(time))
        else:
            self.time = time

    def __str__(self):
        return self.formatservice()

    def formathealth(self):
        return ircutils.mircColor(self.health, "green" if self.status == "good" else ("orange" if self.status == "minor" else "red"))

    def formatname(self):
        return ircutils.bold(self.name)

    def formattime(self):
        return relativedates.timesince(self.time)

    def formatservice(self):
        response = self.formatname() + ": " + self.formathealth()

        if self.time:
            response += " (since " + self.formattime() + ")"

        return response

def create_service(key, name, service):
    return Steamservice(name, key, service["status"], service["title"], service["time"] if "time" in service else None)