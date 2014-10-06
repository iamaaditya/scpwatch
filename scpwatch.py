#!/usr/bin/env python
import sys
import time
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class ScpWatcher(FileSystemEventHandler):
    def __init__(self, file_path, server):
        self.file_to_watch = file_path
        self.server = server

    def on_created(self, event):
        if os.path.basename(self.file_to_watch) == os.path.basename(event.src_path):
            print "%s has been changed. Uploading to %s..." % (self.file_to_watch, self.server)
            args = " %s %s" % (self.file_to_watch, self.server)
            if self.server.count(':') == 0:
                args += ":"
            os.system("scp " + args)

if len(sys.argv) < 3:
    print 'usage: %s <file to watch> <server address> [<path on the server>]' % sys.argv[0]
    print '<path to server> is optional and if it is not passed the file will be copied to the home directory.'
    sys.exit(1)

path   = sys.argv[1]
server = sys.argv[2]

dirpath = os.path.dirname(sys.argv[1])

observer = Observer()
observer.schedule(ScpWatcher(path, server), dirpath, recursive=True)
observer.start()
print "Started watching %s" % path

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
