import pyb
import utime

adc0 = pyb.ADC(pyb.Pin.board.PC0)
print(adc0.read())
