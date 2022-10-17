from os import scandir, rename
from os.path import splitext, exists, join
from time import sleep
from shutil import move
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "C:\\Users\\USER\\Downloads"
image_dir = "C:\\Users\\USER\\Downloads\\Images"
pdf_dir = "C:\\Users\\USER\\Downloads\\PDF"

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

def make_unique(dest, name):
    filename, ext = splitext(name)
    c=1
    while exists(f"{dest}\\{name}"):
        name = f"{filename}({str(c)}){ext}"
        c +=1
    return name


def move_files(dest, entry, name):
    if exists(f"{dest}\\{name}"):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        newName = join(dest, unique_name)
        rename(old_name, newName)
    move(entry, dest)

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_image_files(entry, name)
                self.check_doc_files(entry, name)

    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                dest = image_dir
                move_files(dest, entry, name)
                logging.info(f"Moved file: {name}")
    
    def check_doc_files(self, entry, name):
        if name.endswith(".pdf"):
            dest = pdf_dir
            move_files(dest, entry, name)
            logging.info(f"Moved file: {name}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
