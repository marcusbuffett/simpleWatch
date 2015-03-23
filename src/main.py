"""
Some kind of docstring.
"""

import subprocess
from fnmatch import fnmatch
from termcolor import colored
import time
import sys
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class CommandEventHandler(FileSystemEventHandler):
    """
    Override FileSystemEventHandler from watchdog
    """
    def __init__(self, pathsToWatch, command):
        self.command = command
        self.pathsToWatch = pathsToWatch
        self.lastTimeCalled = time.time()
        self.bufferTime = 1.0
        self.lastProcess = None

    def killLastCommand(self):
        if self.lastProcess:
            if self.lastProcess.poll() is None:
                self.lastProcess.kill()

    def executeCommand(self):
        print('')
        print(colored("Changes detected, restarting", 'yellow'))
        self.lastTimeCalled = time.time()
        self.lastProcess = subprocess.Popen(self.command, shell=True)

    def validPath(self, path):
        return any(fnmatch(path, p) for p in self.pathsToWatch)

    def validEvent(self, event):
        if event.event_type in ["modified", "deleted"]:
            if self.validPath(event._src_path):
                return True
        return False

    def bufferTimeElapsed(self):
        elapsedTime = time.time() - self.lastTimeCalled
        if elapsedTime > self.bufferTime:
            return True
        return False
        return True

    def on_any_event(self, event):
        if self.validEvent(event) and self.bufferTimeElapsed():
            self.killLastCommand()
            self.executeCommand()


def uniqueDirs(paths):
    dirs = []
    for path in paths:
        if path not in dirs:
            dirs.append(os.path.dirname(path))
    return dirs


def main():
    """
    main function
    """
    if len(sys.argv) <= 2:
        print(colored("Must supply a command and a file to watch", 'red'))
        sys.exit(0)
    command = sys.argv[1]

    pathsToWatch = sys.argv[2:]
    absPathsToWatch = [os.path.abspath(path) for path in pathsToWatch]

    commandEventHandler = CommandEventHandler(absPathsToWatch, command)
    observer = Observer()
    for d in uniqueDirs(absPathsToWatch):
        observer.schedule(commandEventHandler, d)
    observer.start()

    print(colored("Files to watch for changes : ", 'green'), end="")
    print(pathsToWatch)
    print(colored("Command to run : ", 'green'), end="")
    print(command)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print('')
        print(colored("Exiting", "red"))
        sys.exit(0)


if __name__ == '__main__':
    main()
