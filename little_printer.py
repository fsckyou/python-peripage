#!/usr/bin/env python3
import tempfile
import os
from watchgod import watch
import config
from pathlib import Path
from PIL import Image
from ppa6 import Printer

class Peripage_Printer:
    def __init__(self):
        self.printer_hardware = Printer(config.macaddress,timeout=10)
        self.printer_hardware.connect()
        self.printer_hardware.setPowerTimeout(0xfff0) # will timeout in 45.5 days

    def print_sirius_image(self, path):
        if self.printer_hardware.isConnected():
            with Image.open(path) as im:
                self.printer_hardware.printImage(im)
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
