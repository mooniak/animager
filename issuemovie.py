#!/usr/bin/env python
"""
    issuemovie.py

    By Mark V.

    See http://eptcomic.com/ept1movie.htm for documentation.

    Please send any questions, comments, bug reports, or patches
    to markv@eptcomic.com

License:

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import datetime
from subprocess import Popen, PIPE, check_call
import re
import sys

class Event:
    """Generic Event class.  We use any time we need to sort
    heterogenous time lines.
    """
    def __init__(self, date):
        self.date = date
        self.rank = 100

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        return str(self)

    def __cmp__(self, rhs):
        return cmp((self.date, self.rank), (rhs.date, rhs.rank))

class GitEvent(Event):
    """A commit in a git repository.
    """
    def __init__(self, logline):
        (commit, timestamp) = logline.strip().split()
        self.commit = commit
        self.date = datetime.datetime.fromtimestamp(int(timestamp))
        self.rank = 2

    def __str__(self):
        return (Popen(('git','show','--stat', self.commit),
                      stdout = PIPE).stdout.read())

if(__name__ == "__main__"):
    issue = "001"
    width = 160
    height = int(1.5*width)
    prefix = "IssueMovie/"

    # Figure out which pages we're tracking

    svgs = ["%s/Page-%02d.svg" % (issue, i) for i in xrange(1,25)]

    # Find and order commits

    p = Popen(["git","log",'--pretty=%H %ct',"--"]+svgs,
              stdout = PIPE)
    events = [GitEvent(i) for i in p.stdout]
    events.sort()

    # Initialize everything to empty rectangles

    p = Popen(("inkscape","Template.svg",
               "--export-png=Template.png",
               "-w",str(width),"-h",str(height),
               "-C","-bffffff","-y1.0",),
              stderr = PIPE)
    if(len(p.stderr.read()) > 0):
        sys.stderr.write("Error rendering template\n")
        sys.exit(1)

    for i in xrange(1,25):
        check_call(("cp","Template.png",prefix+"Page-%02d.png" % i))

    stat_re = re.compile("^ (?P<prefix>[\S]*)"
                         "(?P<page>Page-[\d]{2})\.svg"
                         "[\s]+\|[\s]+[\d]+")

    frames = []
    for (n,event) in enumerate(events):
        # Figure out who changed
        for line in Popen(("git","show","--stat",event.commit),
                          stdout = PIPE).stdout:
            p = stat_re.search(line)
            if(p is not None):
                if(p.group("prefix") != issue+"/"):
                    continue

                # Update SVG
                blob = "%s:%s" % (event.commit, "".join((p.group("prefix"),
                                                         p.group("page"),
                                                         ".svg")))
                cat = Popen(("git","cat-file","blob",blob),
                             stdout = PIPE)
                svg = prefix+"temp.svg" 
                open(svg,"w").write(cat.stdout.read())
                if(cat.wait() != 0):
                    print "Error extracting %s" % blob
                    continue

                # N.B.: This is a good place to do any pre-processing
                #       on the extracted SVGs (e.g., for the EPT movie,
                #       we use sed to update some of the paths to the
                #       new location of our pencil bitmaps)

                # Re-render PNG

                png = prefix+p.group("page")+".png" 
                render = Popen(("inkscape",svg,
                                "--export-png="+png,
                                "-w",str(width),"-h",str(height),
                                "-C","-bffffff","-y1.0"),
                               stderr = PIPE)
                if(len(render.stderr.read()) > 0):
                    print "Inkscape error %s" % blob
                    del render
                    continue
                if(render.wait() != 0):
                    print "Error rendering %s" % blob
                    continue

        # Render mosaic
        frame = "%sframe%04d.png" % (prefix,n)
        check_call(["montage","-geometry","%dx%d" % (width,height),
                    "-tile","8x3"]+
                   ["%sPage-%02d.png" % (prefix, i) for i in xrange(1,25)]+
                   [frame])
        frames.append(frame)

