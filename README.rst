fuss - Fedora User Streams
=========================

The Idea
========
fuss is webapp allowing for FAS users to customize a group of fedmsg topics to listen
to. Messages from the bus are filtered and rebroadcast with a new topic. this
topic will be org.fedoraproject.userstreams.<fas_username>

Long Term
=========
Once this is in place users can recieve customized desktop alerts via fedmsg-notify.
However notifications are just one way custom user streams can be used. Digest
Emails, rss feeds, and other systems can be hooked into the user feeds

Sections
========

+ A Pyramid webapp to allow users to customize what topics to listen to
+ Fedmsg consumer to filter and rebroadcast messages.
