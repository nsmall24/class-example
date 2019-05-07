# Draws a sine wave made out of asterisks, forever.

from math import sin, pi
import time

def sine_thing(n):
    return 20*sin(pi*n/20) + 21

def main():
    s = ""
    i = 0
    while True:
        pos = round(sine_thing(i))
        s = "*".rjust(pos)
        print(s)
        i += 1
        time.sleep(1/30)

main()