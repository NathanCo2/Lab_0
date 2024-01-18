import pyb
import cqueue 
import micropython
micropython.alloc_emergency_exception_buf(100)

# Initialize pins/ADC Objects (aka initialize pins)
pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)#Configures pinC0 for Output
#pinB0 = pyb.Pin(pyb.Pin.board.PB0, pyb.Pin.IN)#Configures pinB0 for Input
adcpin = pyb.ADC(pyb.Pin.board.PB0)# Reads ADC


# Initialize the Queue size
Queue_Size = 200
int_queue = cqueue.IntQueue(Queue_Size)

def timer_int(tim_num): 
    """!
    Doxygen style docstring for interrupt callback function
    """
    val = adcpin.read()
    int_queue.put(val)# Puts an integer into the queue
        
def step_response(data):
    """!
    Doxygen style docstring for this function 
    """
    tim_num = pyb.Timer(2)#Creates a timer 
    tim_num.callback(timer_int)#Turns on callback
    tim_num.init(freq=100)#Starts the timer
    pinC0.high()#Sets pin high to turn on voltage to microcontroller
    while not int_queue.full():#Checks if the queue is full
        pass
    tim_num.callback(None)#Turns off the callback
    cur_time = 0
    while int_queue.any():#Checks if anything is the Queue and emptyin it
        adc_value = int_queue.get()#Gets single value from queue
        voltage = (adc_value/4096)*3.3
        print(f"Time ={cur_time}(ms), Voltage ={voltage}(V)")#Prints voltage with corresponding time
        cur_time = cur_time + 10
    pinC0.low()#Resets the pin to run again
    print("End")#Prints End

if __name__ == "__main__":
    step_response(timer_int)
