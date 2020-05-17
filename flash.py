import sys
import serial
import time
from xmodem import XMODEM

# pip3 install --user pyserial
# pip3 install --user xmodem

# Why?
# https://www.silabs.com/community/mcu/32-bit/forum.topic.html/an0042_bootloader--eQGc

ser = serial.Serial('/dev/cu.usbmodem3101', 115200, timeout=None, rtscts=0, dsrdtr=0, xonxoff=0)
ser.baudrate = 115200

def getc(size, timeout=1):
    got = ser.read(size) or None
    if got == b'\x06':
      sys.stderr.write('· ')
    elif got == b'C':
      sys.stderr.write('🚥 ')
    else:
      sys.stderr.write('.({!r})'.format(got))
    return got

def putc(data, timeout=1):
    # sys.stderr.write('.') # (({!r})'.format(data))
    return ser.write(data)  # note that this ignores the timeout

sys.stderr.write('⏳ ')

# putc(b'i')
putc(b'u')

ser.flush()
sys.stderr.flush()

lastLine = ser.readline()

while lastLine != b'Ready\r\n':
  if lastLine != b'i\r\n' and lastLine != b'u\r\n':
    print(lastLine)
  time.sleep(2)
  lastLine = ser.readline()

modem = XMODEM(getc, putc)
stream = open('toboot-boosted.bin', 'rb')

sys.stderr.flush()

modem.send(stream)

putc(b'b')

sys.stderr.write('⌛')

time.sleep(10)

sys.stderr.write('✅')
