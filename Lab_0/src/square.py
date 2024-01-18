"""!
@file square.py
Run real or simulated dynamic response tests and plot the results. This program
demonstrates a way to make a simple GUI with a plot in it. It uses Tkinter, an
old-fashioned and ugly but useful GUI library which is included in Python by
default.

This file is based loosely on an example found at
https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html

@author Spluttflob
@date   2023-12-24 Original program, based on example from above listed source
@copyright (c) 2023 by Spluttflob and released under the GNU Public Licenes V3
"""
import pyb
import utime

#initialize pins
pinC0 = pyb.Pin(pyb.Pin.board.A5, pyb.Pin.OUT_PP)
adc0 = pyb.ADC(pyb.Pin.board.A5)

#run loop until keyboard interrupt (ctrl+c) pressed
while True:
    pinC0.value(0)
    utime.sleep(5) #stopping code, 5 seconds
    print(adc0.read()) #reads value of pin B0
    pinC0.value(1)
    utime.sleep(5)
    print(adc0.read()) #reads value of pin B0
