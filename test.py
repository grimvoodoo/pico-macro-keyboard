import time
from rotary_irq_rp2 import RotaryIRQ
from machine import Pin
from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd


# i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
# I2C_ADDR = i2c.scan()[0]
# lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
#
# btn = Pin(15, Pin.IN, Pin.PULL_DOWN)
# led = Pin(21, Pin.OUT)
#
# def toggle():
#     led.toggle()
#     sleep(0.2)
#     led.toggle()
#
#
# # start of rotary code section
# SW=Pin(18,Pin.IN,Pin.PULL_UP)
# r = RotaryIRQ(pin_num_clk=17,
#        pin_num_dt=16,
#        min_val=0,
#        reverse=False,
#        range_mode=RotaryIRQ.RANGE_UNBOUNDED)
# val_old = r.value()
# while True:
#   try:
#     led.value(False)
# #     print(I2C_ADDR)
#     lcd.blink_cursor_on()
# #     lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
# #     lcd.putstr("Tom's Hardware")
# #     sleep(2)
# #     lcd.clear()
# #     lcd.putstr("I2C Address:"+str(hex(I2C_ADDR))+"\n")
# #     lcd.putstr("Tom's Hardware")
# #     sleep(2)
# #     lcd.blink_cursor_off()
# #     lcd.clear()
# #     lcd.putstr("Backlight Test")
# #     for i in range(10):
# #         lcd.backlight_on()
# #         sleep(0.2)
# #         lcd.backlight_off()
# #         sleep(0.2)
#     lcd.backlight_on()
# #     lcd.hide_cursor()
# #     for i in range(20):
# #         lcd.putstr(str(i))
# #         sleep(0.4)
# #         lcd.clear()
#     val_new = r.value()
#     if btn.value():
#         print("button prerssed")
#         led.toggle()
#         lcd.clear()
#         lcd.putstr("Button Pressed""\n""\n")
#         sleep(0.5)
#         led.toggle()
#     if SW.value()==0 and n==0:
#       print("Button Pressed")
#       led = Pin(20,Pin.OUT)
#       sleep(0.2)
#       led = Pin(20,Pin.IN)
# #       led.toggle()
# #       sleep(0.1)
# #       led.toggle()
#       lcd.putstr("Button Pressed""\n""\n")
#       print("Selected Number is : ",val_new)
#       n=1
#       while SW.value()==0:
#         continue
#     n=0
#     if val_old != val_new:
#       val_old = val_new
#       print('result =', val_new)
#       led = Pin(20,Pin.OUT)
#       sleep(0.2)
#       led = Pin(20,Pin.IN)
# #       led.toggle()
#       lcd.clear()
#       lcd.putstr("Mode: "+str(val_new)+"\n""\n")
#       sleep(0.0)
#       time.sleep_ms(50)
#   except KeyboardInterrupt:
#     break
