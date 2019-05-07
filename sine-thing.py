from math import sin
import time

PI = 3.14159265358979

def sine_thing(n):
    return 20*sin(PI*n/20) + 21

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