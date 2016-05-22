# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:33:29 2016

@author: Annakoppad
"""

import serial
#import time
#import wmi

import serial.tools.list_ports


ports = list(serial.tools.list_ports.comports())
print "1", ports
for p in ports:
    print p, "here"

print "2"

def scan():
   # scan for available ports. return a list of tuples (num, name)
   available = []
   for i in range(256):
       try:
           s = serial.Serial(i)
           available.append( (i, s.portstr))
           s.close()
       except serial.SerialException:
           pass
   return available

print "Found ports:"
for n,s in scan(): print "(%d) %s" % (n,s)

"""def sendsmstomobile(to, message):
    print "Connecting to mobile"
    c=wmi.WMI()
    modem = c.query("SELECT * FROM Win32_POTSModem").pop()
    print  "here is the modem", modem
    mobserial=serial.Serial(modem.AttachedTo, modem.MaxBaudRateToSerialPort)
    time.sleep(1)
    mobserial.write('ATZ\r')
    time.sleep(1)
    mobserial.write('AT+CMGF=1\r')
    time.sleep(1)
    mobserial.write('''AT+CMGS="'''+ to + '''"\r''')
    time.sleep(1)
    mobserial.write(message+"\r")
    time.sleep(1)
    mobserial.write(chr(26))
    time.sleep(1)

    print "disconnecting from mobile"
    mobserial.close()

print "Filling in the message details"
sendsmstomobile("918792879112", "SMS sent using AT command through Python")
"""