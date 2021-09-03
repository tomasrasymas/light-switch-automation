# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from wifi import Wifi
from servo import Servo

servo_motor = Servo()
servo_motor.reset()

Wifi.connect()