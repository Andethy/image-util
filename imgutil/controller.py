from imgutil.compression.compressor import Compressor
from imgutil.files.manager import ImageDirectory


class FunctionController:
    def __init__(self):
        self.compressor = Compressor()

    def compress(self):
        import tkinter as tk
        from tkinter import filedialog

        print("Select a folder (ALL images in ALL subdirectories will be included as well)")
        # Create a Tkinter root window (it won't be shown)
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        directory_path = filedialog.askdirectory()

        print("Do you want to replace the images (Y/N)")
        wants_replace = True if input().lower() == 'y' else False
        # Open a directory selection dialog

        directory = ImageDirectory(directory_path)
        for item in directory.list_all_files():
            self.compressor.compress_img(item, replace=wants_replace)
        print("!!!Operation complete!!!")
