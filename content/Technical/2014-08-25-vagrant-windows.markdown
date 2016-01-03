---
layout: post
title: Vagrant on Windows
date: 2014-08-25 07:05:00
tags: Process
---
My Dell laptop came preinstalled with Ubuntu Linux. I thought this was pretty cool, but there were annoying issues with my networking driver that I could never resolve. I finally said screw it and started running a clean install of Windows 8.1. I reasoned that I could use Windows for personal computing and virtualization for development environments.

In case any readers were swayed by my [earlier post on Vagrant]({% post_url 2014-08-19-vagrant-intro %}) and want to use it on a Windows machine, here are some traps to watch out for.

Running Virtualbox
-------------------

I chose [Virtualbox][virtualbox] as my virtualization provider. Unfortunately, the most recent stable release doesn’t play well with common Windows antivirus software. The Pitt IT department installed Symantec antivirus on my computer when I switched to Windows. The way Symantec guards against .dll injection prevented Virtualbox from working on my machine. I just uninstalled Symantec and enabled the Windows Defender antivirus instead.

End of the Line
---------------

End of line characters present a thornier issue. UNIX-like systems like Mac OSX and Linux use a line feed (LF) character to denote the end of a line in a text file. Windows uses a carriage return and then a line feed (CRLF). The whole notion of these characters survives from the days of using teletypes as human-machine interfaces. 

So, what happens when you compose a bash script on a Windows host OS and try to run it on a Linux guest OS? Bad things. I switched the settings in my text editor (Sublime) to Unix-style line endings and that solved the immediate problem.

But What about Git?
-------------------

Still, I fretted about what would happen when I committed my files to source control. As is recommended for Windows developers, I had configured Git to automatically convert text files to LF line endings on commit and convert back to CRLF when I bring them into a working directory (this is stored in the [coreauto.crlf][gitLines] setting). I reasoned that having files in the same directory needing different line endings would throw up some issues. After all, the Vagrantfile is read on Windows, but shell scripts and actual project code is read on Linux. I researched the issue and looked into configuring .gitattributes files and changing my git coreauto.crlf settings on a per-repository basis. 

Then I decided that I should first try committing and pulling in the naïve, Windows-default fashion. And I haven’t had any problems! While I’m pleased that I don’t need to do any more config twiddling, I’m still unsettled. I don’t understand how these line endings are taking care of themselves. If I see any strange behavior in the future, I’ll have a likely suspect. 

[virtualbox]: https://www.virtualbox.org/
[gitLines]: http://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/