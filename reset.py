import sys
import serial
import time

# pip3 install --user pyserial
# pip3 install --user xmodem

# Why?
# https://www.silabs.com/community/mcu/32-bit/forum.topic.html/an0042_bootloader--eQGc

ser = serial.Serial('/dev/cu.usbmodem3101', 115200, timeout=None, rtscts=0, dsrdtr=0, xonxoff=0)
ser.baudrate = 115200

def putc(data, timeout=1):
    # sys.stderr.write('.') # (({!r})'.format(data))
    return ser.write(data)  # note that this ignores the timeout

sys.stderr.write('⏳ ')

putc(b'r')

sys.stderr.write('⌛️ ✅')
