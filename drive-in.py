#!/usr/bin/env python3

from raepy import Servo, Rack
import time

if __name__ == "__main__":
    s = Servo()
    r = Rack()
    r.home()

    for i in range(300):
        print("In Cycle: {}".format(i))
        r.to(0.06)
        time.sleep(0.5)
        r.to(0)
        time.sleep(0.5)

    s.limp()