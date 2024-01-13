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
