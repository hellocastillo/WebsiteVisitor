# Edgar Castillo / Github: https://github.com/hellocastillo
# Copyright (c) 2021 Edgar Castillo

import webbrowser
import time
from pykeyboard import PyKeyboard

count = 0
# If used, this program will route your towards my Github lol.
urls = ['https://github.com/hellocastillo/Data-Structures-Algorithms', 'https://github.com/hellocastillo',
        'hhttps://github.com/hellocastillo/Python-Spammer']
k = PyKeyboard()

while count < 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
        k.press_keys(['Command', 'W'])
        count = count + 1

else:
    pass
