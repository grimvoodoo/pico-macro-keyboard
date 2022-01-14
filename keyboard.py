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

# Functions

def led_toggle():
    led.toggle()
    sleep(0.2)
    led.toggle()


# def execute():
while True:  
  try:
    led.value(False)
#         lcd.blink_cursor_off()
    lcd.backlight_on()
    val_new = r.value()
    if btn.value():
        print("button prerssed")
        led_toggle()
    if SW.value()==0 and n==0:  
      print("Button Pressed")
      led = Pin(20,Pin.OUT)
      sleep(0.2)
      led = Pin(20,Pin.IN)
#       led.toggle()
#       sleep(0.1)
#       led.toggle()
      lcd.putstr("Button Pressed""\n""\n")
      print("Selected Number is : ",val_new)  
      n=1  
      while SW.value()==0:  
        continue  
    n=0  
    if val_old != val_new:  
      val_old = val_new  
      print('result =', val_new)
      led = Pin(20,Pin.OUT)
      sleep(0.2)
      led = Pin(20,Pin.IN)
#       led.toggle()
      lcd.clear()
      lcd.putstr("Mode: "+str(val_new)+"\n""\n")
      sleep(0.0)
      time.sleep_ms(50)  
  except KeyboardInterrupt:  
    break  


# execution

execute()
