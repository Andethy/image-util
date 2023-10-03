import sys
from os import path, rename
from pathlib import Path


class ImageDirectory:

    def __init__(self, abs_path, valid_extensions=("png", "jpg", "jpeg")):
        self.dir_path = Path(abs_path)
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

    def lowercase_all_files(self):
        for item in self.files:
            rename(item, path.join(path.dirname(item), path.basename(item).lower()))
        for item in self.dirs:
            item.lowercase_all_files()

    def reset_all_files_counter(self, places):
        for item in self.files:
            count = ''
            is_num = False
            end_index = len(path.basename(item))
            for char in item[::-1]:
                end_index -= 1
                if char == '.':
                    is_num = True
                elif not char.isnumeric() and is_num:
                    break
                elif is_num:
                    count = char + count
            count = str(int(count))
            new_base = path.basename(item)[:end_index] + "_" + "0" * (places - len(count)) + count + Path(item).suffix
            rename(item, path.join(path.dirname(item), new_base))
            print("[~] Renamed to", new_base)
        for item in self.dirs:
            item.reset_all_files_counter(places)



if __name__ == '__main__':
    directory = ImageDirectory("/Users/jackhayley/Downloads/Orlando_Portfolio")
    print(directory.reset_all_files_counter(2))
