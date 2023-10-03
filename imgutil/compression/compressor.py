import os
import argparse

from PIL import Image


class Compressor:
    def __init__(self):
        self.monitor = CompMonitor()

    def start(self):
        self.monitor.create_parser()
        self.compress_img(self.monitor.get_img())

    def compress_img(self, image_name, new_size_ratio=0.5, quality=90, width=None, height=None, to_jpg=True, replace=True):
        # load the image to memory
        img = Image.open(image_name)
        # print the original image shape
        print("[*] Image shape:", img.size)
        # get the original image size in bytes
        image_size = os.path.getsize(image_name)
        # print the size before compression/resizing
        print("[*] Size before compression:", self.monitor.get_size_format(image_size))
        if new_size_ratio < 1.0:
            # if resizing ratio is below 1.0, then multiply width & height with this ratio to reduce image size
            img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.LANCZOS)
            # print new image shape
            print("[+] New Image shape:", img.size)
        elif width and height:
            # if width and height are set, resize with them instead
            img = img.resize((width, height), Image.LANCZOS)
            # print new image shape
            print("[+] New Image shape:", img.size)
        # split the filename and extension
        filename, ext = os.path.splitext(image_name)
        # make new filename appending _compressed to the original file name
        add = '' if replace else '_comp';
        if to_jpg:
            # change the extension to JPEG
            new_filename = f"{filename + add}.jpg"
        else:
            # retain the same extension of the original image
            new_filename = f"{filename + add}{ext}"
        try:
            # save the image with the corresponding quality and optimize set to True
            img.save(new_filename, quality=quality, optimize=True)
        except OSError:
            # convert the image to RGB mode first
            img = img.convert("RGB")
            # save the image with the corresponding quality and optimize set to True
            img.save(new_filename, quality=quality, optimize=True)
        print("[+] New file saved:", new_filename)
        # get the new image size in bytes
        new_image_size = os.path.getsize(new_filename)
        # print the new size in a good format
        print("[+] Size after compression:", self.monitor.get_size_format(new_image_size))
        # calculate the saving bytes
        saving_diff = new_image_size - image_size
        # print the saving percentage
        print(f"[+] Image size change: {saving_diff / image_size * 100:.2f}% of the original image size.")


class CompMonitor:
    units = ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']

    def __init__(self, factor=1024, suffix='B'):
        self.factor = factor
        self.suffix = suffix
        self.parser = argparse.ArgumentParser(description="Simple Python script for compressing and resizing images")
        self._args = None

    def get_size_format(self, b: int):
        """
        Scale bytes to its proper byte format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        for unit in CompMonitor.units:
            if b < self.factor:
                return f'{b:.2f}{unit}{self.suffix}'
            b /= self.factor
        return f'{b:.2f}Y{self.suffix}'

    def change_units(self, factor, suffix):
        self.factor = factor
        self.suffix = suffix

    def create_parser(self):
        self.parser.add_argument("image", help="Target image to compress and/or resize")
        self.parser.add_argument("-j", "--to-jpg", action="store_true",
                                 help="Whether to convert the image to the JPEG format")
        self.parser.add_argument("-q", "--quality", type=int,
                                 help="Quality ranging from a minimum of 0 (worst) to a maximum of 95 (best). Default "
                                      "is 90",
                                 default=90)
        self.parser.add_argument("-r", "--resize-ratio", type=float,
                                 help="Resizing ratio from 0 to 1, setting to 0.5 will multiply width & height of the "
                                      "image by 0.5. Default is 1.0",
                                 default=1.0)
        self.parser.add_argument("-w", "--width", type=int,
                                 help="The new width image, make sure to set it with the `height` parameter")
        self.parser.add_argument("-hh", "--height", type=int,
                                 help="The new height for the image, make sure to set it with the `width` parameter")
        self._args = self.parser.parse_args();

    def get_args(self):
        return self._args

    def get_img(self):
        return self._args.image


if __name__ == '__main__':
    comp = Compressor()
    comp.start()

