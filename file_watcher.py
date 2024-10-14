import os
import sys
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class ReloadHandler(FileSystemEventHandler):
    # According to ChatGPT, need this function when instance of ReloadHandler created
    # Takes the name of the script to monitor
    def __init__(self, script_to_run): 
        self.script_to_run = script_to_run # Storing the scipt name in an "instance" variable

    def on_modified(self, event):
        print(f"Detected modification: {event.src_path}")
        print(f"Watching script: {self.script_to_run}")
        # Check if the modified file is the one you're watching
        if event.src_path.endswith(self.script_to_run):
            print(f"{self.script_to_run} modified! Restarting the scipt...")
            self.restart_script()

    def restart_script(self):
        # Full path of the script to restart
        script_path = os.path.join(os.getcwd(), self.script_to_run)
        print(f"Restarting script: {script_path}")

        # os.execv set to replace current running process with a new one
        # sys.executable provides path to Python interpreter
        os.execv(sys.executable, ['python'] + [self.script_to_run])

def start_watching(script_to_run):
    # Here we create instance of ReloadHandler with script name
    event_handler = ReloadHandler(script_to_run)

    # Now we create an Observer instance to monitor the file system
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    print(f"Watching {script_to_run} for any changes...")
    return observer


# The following only runs if script is executed directly, not imported as module.
if __name__ == "__main__":
    script_file = 'python-clipboard-redactor.py'
    observer = start_watching(script_file)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() # Waiting for the observer thread to finish before exiting

