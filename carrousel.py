#!/usr/bin/python

import webview
import threading

import time
import sys

import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



def show_carrousel():
    time.sleep(5)
    while True:
        script = [line.rstrip('\n') for line in open('carrousel1.txt')]  
        for line in script: 
            if (line == "quit"):
               webview.destroy_window()
               sys.exit(0)
            try:
                page,timeout=line.split(',')
                print page
                webview.load_url(page)
                time.sleep(int(timeout))
            except:
                print "ERROR:",line

if __name__ == '__main__':
  
    t = threading.Thread(target=show_carrousel)
    t.start()

    webview.create_window("Carrousel", "carrousel.html", fullscreen=True)


