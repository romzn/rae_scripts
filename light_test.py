#! /usr/bin/env python3
from raepy import LedButton
import time

perception_system = "kinect"

if __name__ == "__main__":
    if perception_system == "realsense":
        lb = LedButton()
        lb.led.heartbeat_on(speed=1)
        time.sleep(30)
        lb.led.heartbeat_off()
        lb.led.blink(freq=12,cnt=17)
        lb.led.heartbeat_on(speed=100)
        time.sleep(10)
        lb.led.heartbeat_off()

    elif perception_system == "kinect":
        lb1 = LedButton()
        lb2 = LedButton(ledpin=16,buttonpin=18)
        lb1.led.heartbeat_on(speed=1)
        lb2.led.heartbeat_on(speed=1)
        time.sleep(30)
        lb1.led.heartbeat_off()
        lb2.led.heartbeat_off()
        lb1.led.blink_on(freq=12)
        lb2.led.blink_on(freq=12)
        time.sleep(2)
        lb1.led.stop_blink()
        lb2.led.stop_blink()
        lb1.led.heartbeat_on(speed=100)
        lb2.led.heartbeat_on(speed=100)
        time.sleep(10)
        lb1.led.heartbeat_off()
        lb2.led.heartbeat_off()
    
    





