#!/usr/bin/env python3
import tempfile
import os
from watchgod import watch
import config
from pathlib import Path
from PIL import Image, ImageOps
from ppa6 import Printer

class Peripage_Printer:
    def __init__(self):
        self.printer_hardware = Printer(config.macaddress,timeout=10)
        self.printer_hardware.connect()
        self.printer_hardware.setPowerTimeout(0xfff0) # will timeout in 45.5 days

    def print_sirius_image(self, path):
        if self.printer_hardware.isConnected():
            with Image.open(path) as img:
                # This image manipulation can be done directly in ppa6 using the
                # printImage() method, BUT it forces delay=0.1 (not matching the
                # documentation). delay=0 is WAY better looking so we use
                # printImageBytes().
                img = img.convert('L')
                img = ImageOps.invert(img)
                img = img.resize((self.printer_hardware.getRowWidth(), int(self.printer_hardware.getRowWidth() / img.size[0] * img.size[1])), Image.NEAREST)
                img = img.convert('1')
        
                imgbytes = img.tobytes()
                self.printer_hardware.printImageBytes(imgbytes, delay=0)
            self.printer_hardware.printBreak()

if __name__ == '__main__':
    mmj=Peripage_Printer()
    # `sirius-client` will write to this folder
    tmpdir = os.path.join(tempfile.gettempdir(), 'sirius-client')
    Path(tmpdir).mkdir(parents=True, exist_ok=True)
    
    for changes in watch(tmpdir):
        file = changes.pop()[1] 
        print("Printing " + file)
        mmj.print_sirius_image(file)
