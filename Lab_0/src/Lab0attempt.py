
  """! @file main.py
  Doxygen style docstring for the file 
  """
import pyb
import utime
from cqueue import IntQueue as Queue
import micropython
micropython.alloc_emergency_exception_buf(100)

# Make pins/ADC Objects (aka initialize pins)
pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)# (Pin.OUT_PP) configures the pin for output, with push-oull control
pinB0 = pyb.Pin(pyb.Pin.board.PB0, pyb.Pin.OUT_PP)

adc0 = pyb.ADC(pinB0) #To read the ADC 

  def timer_int(tim_num):
      """!
      Doxygen style docstring for interrupt callback function
      """
      adcpin = pyb.ADC (pinB0)# Reads ADC
      Queue.put(int data)# Stores data in queue 

  def step_response (...parameters...):
      """!
      Doxygen style docstring for this function 
      """
      adc = pyb.ADC(pyb.Pin.board.PC0)#creates an ADC on pin PB0
      tim = pyb.Timer(1, freq=100)#creates a timer running (turns on callback?)
      tim.callback(timer_int)#turns on callback
      pinC0.high()#sets pin high to trigger step
      if Queue.full()#checks if the queue is full
      tim.callback(NONE)#turns off the callback
      for data in Queue:
          print(tim, data)#prints data line by line
      print ("End")#print End
      pinC0.low()# Resets the Pin to run again 


  if __name__ == "__main__":
      step_response(...parameters...)