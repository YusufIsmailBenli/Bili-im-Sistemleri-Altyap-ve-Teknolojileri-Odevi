import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        log_event = {
            "event": "created",
            "path": event.src_path,
            
        }
        self.log_event(log_event)


    def on_deleted(self, event):
        if event.is_directory:
            return
        
        log_event = {
            "event": "deleted",
            "path": event.src_path,
            
        }
        self.log_event(log_event)

    def on_moved(self, event):
        if event.is_directory:
            return
        
        print(f"Moved file: {event.src_path} -> {event.dest_path}")
        
        log_event = {
            "event": "renamed",
            "old_file": event.src_path,
            "new_file": event.dest_path,
            
        }
        self.log_event(log_event)

    def log_event(self, log_event):
        log_file_path = "/home/yusuf/bsm/logs/changes.json"
        
        try:
            with open(log_file_path, "r") as log_file:
                data = json.load(log_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(log_event)

        with open(log_file_path, "w") as log_file:
            json.dump(data, log_file, indent=2)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path="/home/yusuf/bsm/test", recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

