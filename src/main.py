"""
Some kind of docstring.
"""

import subprocess
from termcolor import colored
import time
import sys
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class CommandEventHandler(FileSystemEventHandler):
    """
    Override FileSystemEventHandler
    """
    def __init__(self, filePath, command):
        self.command = command
        self.filePath = filePath
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

    def validEvent(self, event):
        if event.event_type in ["modified", "deleted"]:
            if event._src_path == self.filePath:
                return True
        return False

    def bufferTimeElapsed(self):
        elapsedTime = time.time() - self.lastTimeCalled
        if elapsedTime > self.bufferTime:
            return True
        return False

    def on_any_event(self, event):
        if self.validEvent(event) and self.bufferTimeElapsed():
                self.killLastCommand()
                self.executeCommand()


def main():
    """
    main function
    """
    if len(sys.argv) <= 2:
        print(colored("Must supply a command and a file to watch", 'red'))
        sys.exit(0)
    command = sys.argv[1]
    filePath = sys.argv[2]
    absPath = os.path.abspath(filePath)

    commandEventHandler = CommandEventHandler(absPath, command)
    observer = Observer()
    observer.schedule(commandEventHandler, os.path.dirname(absPath))
    observer.start()

    print(colored("Path to watch for changes : " + filePath, 'green'))
    print(colored("Command to run : " + command, 'green'))
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
