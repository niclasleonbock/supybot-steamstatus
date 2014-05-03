supybot-steamstatus
===================

This supybot plugin fetches Steam status information from steamstat.us when someone issues the "steam" command.

Commands
=========
**steam / steamservice** ***[service key]*** - takes no or one argument(s), issued without any arguments it just returns the status of default steam services, if issued with one argument it returns the status of the specified steam service, fetched from steamstat.us

**steamservices** - takes no arguments, lists all available steam service keys (that may be used with steam / steamservice)
