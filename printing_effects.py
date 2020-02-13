import time
import os
import sys
import msvcrt as m


def delay_print(s,t):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)
        
def wait():
    m.getch()

# print("Hello there.")
# wait()
# delay_print("Okay then.",0.5)
# wait()
# print("No, you boomer.")