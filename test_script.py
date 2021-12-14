#!/usr/bin/python

import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1

# Split an integer input into a two byte array to send via SPI
def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

# Repeatedly switch a MCP4151 digital pot off then on
while True:
    write_pot(10000001)
    #time.sleep(.05)
    write_pot(11)
    #time.sleep(.05)
