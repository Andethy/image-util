from imgutil.compression.compressor import Compressor
from imgutil.files.manager import ImageDirectory


class FunctionController:
    def __init__(self):
        self.compressor = Compressor()

    def compress(self):
        print("Select a folder (ALL images in ALL subdirectories will be included as well)")
        directory_path = self._get_dir_path()

        print("Do you want to replace the images (Y/N)")
        wants_replace = True if input().lower() == 'y' else False
        # Open a directory selection dialog

        directory = ImageDirectory(directory_path)
        for item in directory.list_all_files():
            self.compressor.compress_img(item, replace=wants_replace)
        print("!!!Operation complete!!!")

    def lower_imgs(self):
        print("Select a folder (ALL images in ALL subdirectories will be included as well)")
        directory_path = self._get_dir_path()
        ImageDirectory(directory_path).lowercase_all_files()
        print("!!!Operation complete!!!")

    @staticmethod
    def _get_dir_path():
        import tkinter as tk
        from tkinter import filedialog
        # Create a Tkinter root window (it won't be shown)
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        return filedialog.askdirectory();

    def change_idx(self):
        print("Select a folder (ALL images in ALL subdirectories will be included as well)")
        directory_path = self._get_dir_path()
        print("How many 0s do you want in from the the images (MUST be formatted <name>_0...<number>.<extension>")
        x = int(input())
        ImageDirectory(directory_path).reset_all_files_counter(x)
        print("!!!Operation complete!!!")
