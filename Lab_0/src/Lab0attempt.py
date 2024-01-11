
  """! @file main.py
  Doxygen style docstring for the file 
  """
import pyb
import utime
import micropython
micropython.alloc_emergency_exception_buf(100)

# Make pins/ADC Objects (aka initialize pins)
pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)# (Pin.OUT_PP) configures the pin for output, with push-oull control
adc0 = pyb.ADC(pyb.Pin.board.PC0) #To read the ADC 

  def timer_int(tim_num):
      """!
      Doxygen style docstring for interrupt callback function
      """
      adcpin = pyb.ADC (pyb.Pin.board.PC0)# Reads ADC
      def cqueue.IntQueue.put(int data)# Stores data in queue 

  def step_response (...parameters...):
      """!
      Doxygen style docstring for this function 
      """
      adc = pyb.ADC(pyb.Pin.board.PC0)#creates an ADC on pin PB0
      tim = pyb.Timer(1, freq=100)#creates a timer running (turns on callback?)
      pinC0.high()#sets pin high to trigger step
    
      val = adc.read_vref()#reads MCU supply voltage
      print ("End")
      pinC0.low()# Resets the Pin to run again 


  if __name__ == "__main__":
      step_response(...parameters...)