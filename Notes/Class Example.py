import pyb
import utime

adc0 = pyb.ADC(pyb.Pin.board.PC0)
print(adc0.read())


if utime.ticks_diff(ticks1, ticks2) > 5000
ticks1 = utime.ticks_ms() #gives current time on board
utime.ticks_diff(5000, ticks1) #lets us take difference between times