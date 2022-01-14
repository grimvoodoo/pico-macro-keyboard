import time  
from rotary_irq_rp2 import RotaryIRQ  
from machine import Pin
from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
# def initialise():
# LCD screen vars
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# LED vars
led = Pin(21, Pin.OUT)

# button vars
btn = Pin(15, Pin.IN, Pin.PULL_DOWN)

# start of rotary code section
SW=Pin(18,Pin.IN,Pin.PULL_UP)  
r = RotaryIRQ(pin_num_clk=17,   
       pin_num_dt=16,   
       min_val=0,   
       reverse=False,   
       range_mode=RotaryIRQ.RANGE_UNBOUNDED)  
val_old = r.value()
