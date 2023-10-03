import sys
from os import path
from pathlib import Path


class ImageDirectory:

    def __init__(self, directory, valid_extensions = ("png", "jpg", "jpeg")):
        self.dir_path = Path(directory)
        self.valid_ext = valid_extensions
        self.files = []
        self.dirs = []
        for item in self.dir_path.iterdir():
            if path.isfile(item) and Path(item).suffix.strip('.').lower() in self.valid_ext:
                self.files.append(path.abspath(item))
            elif path.isdir(item):
                self.dirs.append(ImageDirectory(path.abspath(item)))

    def list_all_files(self):
        files = self.files.copy()
        for item in self.dirs:
            files += item.list_all_files()
        return files


if __name__ == '__main__':
    directory = ImageDirectory(sys.argv[0])
    print(directory.list_all_files())


