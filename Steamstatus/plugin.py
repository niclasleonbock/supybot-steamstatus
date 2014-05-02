###
# Copyright (c) 2014, Niclas Leon Bock
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###
import json
import datetime

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

class Steamstatus(callbacks.Plugin):
    """Just type in 'steam' as command and have fun."""

    threaded = True

    url = "http://steamstat.us/status.json"
    services = { "Community": "community",
                 "Store": "store",
                 "Client": "steam",
                 "CS:Go": "csgo_community" }

    def fetch(self):
        return json.loads(utils.web.getUrl(self.url))

    def steam(self, irc, msg, args):
        """takes no  arguments

        Returns steams status fetched from steamstat.us
        """

        status = self.fetch()
        response = "Steamstatus: "

        if len(self.services) < 1:
            irc.error("No services defined.", True)

        for (name, key) in self.services.items():
            service = status["services"][key]
            response += ircutils.bold(name + ": ")
            response += ircutils.mircColor(service["title"], "green" if service["status"] == "good" else ("orange" if service["status"] == "minor" else "red"))

            if "time" in service:
                response += " (" + datetime.datetime.fromtimestamp(int(service["time"])).strftime("%Y-%m-%d %H:%M:%S") + ")"

            response += ", "

        irc.reply(response[:-2])

Class = Steamstatus

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79: