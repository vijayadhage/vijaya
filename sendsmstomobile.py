'''
Send messages to mobile via mobile
Author: Annapoornima KOppad
Date: 16-May-2016
'''

import serial
import time

def sendsmstomobile(to, message):
    print "Connecting to mobile"

    mobserial=serial.Serial('/dev/ttyACM0', 460800, timeout=5)
    time.sleep(1)
    ser.write('ATZ\r')
    time.sleep(1)
    ser.write('AT+CMGF=1\r')
    time.sleep(1)
    ser.write('''AT+CMGS="'''+ to + '''"\r''')
    time.sleep(1)
    ser.write(message+"\r")
    time.sleep(1)
    ser.write(chr(26))
    time.sleep(1)

    print "disconnecting from mobile"
    ser.close()

print "Filling in the message details"
sendsmstomobile("918792879112", "SMS sent using AT command through Python")
