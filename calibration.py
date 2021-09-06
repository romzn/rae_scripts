#! /usr/bin/env python3
from raepy import LedButton, Rack, RadialGripper, Servo
import time
rack = Rack()
gripper = RadialGripper()
servo = Servo()


if __name__ == "__main__":    
    rack.home()
    gripper.set_fingerlength(0.15)
    gripper.calibrate()
    gripper.to(0.1)
    servo.limp()

    
    





