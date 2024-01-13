"""! @file main.py
Doxygen style docstring for the file 
"""
import pyb
import utime

timmy = pyb.Time (1, freq = 100)
timmy.counter ()

pinC0 = pyb.Pin(pyb.Pin.board.A5, pyb.Pin.OUT_PP)
adc0 = pyb.ADC(pyb.Pin.board.A3)

def timer_int(tim_num):
  """!
  Doxygen style docstring for interrupt callback function
  """
  print(timmy.counter(),adc0.read()) 
  cqueue.IntQueue
      
timmy.callback timer_int

  def step_response (...parameters...):
      """!
      Doxygen style docstring for this function 
      """
      pinC0.value(0)
      utime.sleep(5) #stopping code, 5 seconds
      pinC0.value(0)
      utime.sleep(5) #stopping code, 5 seconds


  if __name__ == "__main__":
      step_response(...parameters...)
        