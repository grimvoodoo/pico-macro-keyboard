import time  
from rotary_irq_rp2 import RotaryIRQ  
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from machine import Pin, Timer, time_pulse_us
led = Pin(22, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

# timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)


from rotary_irq_rp2 import RotaryIRQ  
from machine import Pin, Timer
from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd


# def initialise():
# LCD screen vars
try:
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    I2C_ADDR = i2c.scan()[0]
    lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
except:
    print("Screen disconnected")

# LED vars
led = Pin(22, Pin.OUT)

# Timer vars
timer = Timer

# button vars
btn1 = Pin(2, Pin.IN, Pin.PULL_DOWN)
btn2 = Pin(3, Pin.IN, Pin.PULL_DOWN)
btn3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
btn4 = Pin(5, Pin.IN, Pin.PULL_DOWN)
btn5 = Pin(6, Pin.IN, Pin.PULL_DOWN)
btn6 = Pin(7, Pin.IN, Pin.PULL_DOWN)
btn7 = Pin(8, Pin.IN, Pin.PULL_DOWN)
btn8 = Pin(9, Pin.IN, Pin.PULL_DOWN)
btn9 = Pin(10, Pin.IN, Pin.PULL_DOWN)

# start of rotary code section
SW=Pin(18,Pin.IN,Pin.PULL_UP)  
dial = RotaryIRQ(pin_num_clk=17,   
       pin_num_dt=16,   
       min_val=0,   
       reverse=False,   
       range_mode=RotaryIRQ.RANGE_UNBOUNDED)  
val_old = dial.value()

# Functions

def execute():
    global led
    global lcd
    global SW
    global val_old
    global btn1
    global btn2
    global btn2
    global btn3
    global btn4
    global btn5
    global btn6
    global btn7
    global btn8
    global btn9
    
    led.value(False)
    lcd.backlight_on()
    val_new = dial.value()
    
    while True:  
        try:
            
            # logic for combining buttons, like `shift` + `g` for example
#             if btn1.value():
#                 if btn2.value():
#                     lcd.clear()
#                     lcd.putstr("Button 1 + 2 Pressed""\n""\n")
#                     print("btn1+2 pressed")
#                     blink()
            if btn2.value():
                lcd.clear()
                lcd.putstr("Button 2 Pressed""\n""\n")
                print("btn2 pressed")
#                 timer.init(mode=Timer.ONE_SHOT, period=1000, callback=led.toggle())
                time_pulse_us(pin=22, pulse_level=1, timeout_us=1000000)
            if btn3.value():
                lcd.clear()
                lcd.putstr("Button 3 Pressed""\n""\n")
                print("btn3 pressed")
                blink()
            if btn4.value():
                lcd.clear()
                lcd.putstr("Button 4 Pressed""\n""\n")
                print("btn4 pressed")
                blink()
            if btn5.value():
                lcd.clear()
                lcd.putstr("Button 5 Pressed""\n""\n")
                print("btn5 pressed")
                blink()
            if btn6.value():
                lcd.clear()
                lcd.putstr("Button 6 Pressed""\n""\n")
                print("btn6 pressed")
                blink()
            if btn7.value():
                lcd.clear()
                lcd.putstr("Button 7 Pressed""\n""\n")
                print("btn7 pressed")
                blink()
            if btn8.value():
                lcd.clear()
                lcd.putstr("Button 8 Pressed""\n""\n")
                print("btn8 pressed")
                blink()
            if btn9.value():
                lcd.clear()
                lcd.putstr("Button 9 Pressed""\n""\n")
                print("btn9 pressed")
                blink()
            
            
        #         lcd.blink_cursor_off()
            
#             if btn.value():
#                 print("button prerssed")
#                 led_toggle()
                
                
                
            if not SW.value():
                print("Button Pressed")
                sleep(0.2)
                lcd.putstr("Button Pressed""\n""\n")
                print("Selected Number is : ",val_new)
                
                while not SW.value():  
                    continue 
                
            if val_old != val_new:  
              val_old = val_new  
              print('result =', val_new)
              lcd.clear()
              lcd.putstr("Mode: "+str(val_new)+"\n""\n")
              sleep(0.0)
              time.sleep_ms(50)  
        except KeyboardInterrupt:  
            break  


def led_test():
    start = False
    while True:
        # for a single LED
        led = Pin(22, Pin.OUT)
        if not start:
            led.value(False)
            print("starting")
            start = True
        else:
            led.toggle()
            print("toggling")
        sleep(0.2)
        
        # for a range of LED's
#         for i in range(26):
#             led = Pin(i, Pin.OUT)
#             if not start:
#                 led.value(False)
#                 print("starting")
#                 start = True
#             else:
#                 led.toggle()
#                 print("toggling")
#         sleep(0.2)
            

def button_test():
    global led
    global lcd
    global SW
    global val_old
    global btn1
    global btn2
    global btn3
    global btn4
    global btn5
    global btn6
    global btn7
    global btn8
    global btn9
    while True:  
        if btn1.value():
            lcd.clear()
            lcd.putstr("Button 1 Pressed""\n""\n")
            print("btn1 pressed")
        if btn2.value():
            lcd.clear()
            lcd.putstr("Button 2 Pressed""\n""\n")
            print("btn2 pressed")
        if btn3.value():
            lcd.clear()
            lcd.putstr("Button 3 Pressed""\n""\n")
            print("btn3 pressed")
        if btn4.value():
            lcd.clear()
            lcd.putstr("Button 4 Pressed""\n""\n")
            print("btn4 pressed")
        if btn5.value():
            lcd.clear()
            lcd.putstr("Button 5 Pressed""\n""\n")
            print("btn5 pressed")
        if btn6.value():
            lcd.clear()
            lcd.putstr("Button 6 Pressed""\n""\n")
            print("btn6 pressed")
        if btn7.value():
            lcd.clear()
            lcd.putstr("Button 7 Pressed""\n""\n")
            print("btn7 pressed")
        if btn8.value():
            lcd.clear()
            lcd.putstr("Button 8 Pressed""\n""\n")
            print("btn8 pressed")
        if btn9.value():
            lcd.clear()
            lcd.putstr("Button 9 Pressed""\n""\n")
            print("btn9 pressed")

# execution

execute()
# led_test()
# button_test()
