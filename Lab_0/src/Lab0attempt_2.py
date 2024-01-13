import pyb
import utime
from cqueue import IntQueue as Queue
import micropython
micropython.alloc_emergency_exception_buf(100)

# Initialize pins/ADC Objects (aka initialize pins)
pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)#Configures pinC0 for Output
pinB0 = pyb.Pin(pyb.Pin.board.PB0, pyb.Pin.IN)#Configures pinB0 for Input

def timer_int(tim_num): 
    """!
    Doxygen style docstring for interrupt callback function
    """
    adcpin = pyb.ADC(pinB0)# Reads ADC
    Queue.put(adcpin)# Puts an integer into the queue
    
def step_response(data):
    """!
    Doxygen style docstring for this function 
    """
    tim_num = pyb.Timer(1, freq=100)#Creates a timer 
    start_time = utime.ticks_ms()#Starts a timer
    tim_num.callback(timer_int)#Turns on callback
    pinC0.high()#Sets pin high to turn on voltage to microcontroller
    if Queue.full():#Checks if the queue is full
        tim.callback(NONE)#Turns off the callback
        if Queue.empty():#Checks if the Queue is empty
            voltage = Queue.get()#Gets single value from queue
            print(f"Time ={start_time}(ms), Voltage ={voltage}(V)")#Prints voltage with corresponding time
        print("End")#Prints End
        pinC0.low()#Resets the pin to run again

if __name__ == "__main__":
    step_response(timer_int)
