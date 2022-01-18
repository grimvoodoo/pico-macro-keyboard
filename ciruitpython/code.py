import conf
import time
import digitalio
import board
import busio
import rotaryio
import usb_hid
import adafruit_character_lcd.character_lcd as character_lcd
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
# load the LCD library
import lcd
import i2c_pcf8574_interface


keyboard = Keyboard(usb_hid.devices)

i2c = busio.I2C(scl=board.GP1, sda=board.GP0)

iface = i2c_pcf8574_interface.I2CPCF8574Interface(i2c, 0x27)
display = lcd.LCD(iface, num_rows=4, num_cols=20)
display.set_backlight(True)
display.set_display_enabled(True)

# for count in range(10000):
#     display.set_cursor_pos(1, 4)
#     display.print("%04d" % count)
#     print("%04d" % count)
#     time.sleep(1)

# display.print("Hello, world.")

# USB device
# consumer = ConsumerControl(usb_hid.devices)

# button delay
# dl = 0.2

# loop
# while True:
#
#     # poll encoder button
#     if conf.rotate_button.value == 0:
#         consumer.send(ConsumerControlCode.MUTE)
#         conf.led.value = True
#         time.sleep(dl)
#         conf.led.value = False
#     time.sleep(0.1)

# def button(key):
#     btn_pin = getattr(board, key)
#     btn = digitalio.DigitalInOut(btn_pin)
#     btn.direction = digitalio.Direction.INPUT
#     btn.pull = digitalio.Pull.DOWN
#     return btn
#
#
MEDIA = 0xe8
"""Plays and pauses media"""


def key_detection():
    mode = 1
    display.print(f"mode: {mode}")
    display.set_cursor_pos(1,0)
    display.print("Blender Modeling")
    # for x in pin_list:
    #     btn = button(x)
    while True:
        if conf.previous_value != conf.rotate_step.value:
            if not conf.rotate_step.value:
                if not conf.rotate_direction.value:
                    print("Rotated Right")
                    display.clear()
                    display.print("Rotated Right")
                    time.sleep(0.5)
                    if mode < 3:
                        keyboard.release_all()
                        mode += 1
                        display.clear()
                        display.print(f"mode: {mode}")
                    else:
                        keyboard.release_all()
                        mode = 1
                        display.clear()
                        display.print(f"mode: {mode}")
                    time.sleep(0.5)
                else:
                    print("Rotated left")
                    display.clear()
                    display.print("Rotated Left")
                    time.sleep(0.5)
                    if mode > 1:
                        keyboard.release_all()
                        mode -= 1
                        display.clear()
                        display.print(f"mode: {mode}")
                    else:
                        keyboard.release_all()
                        mode = 3
                        display.clear()
                        display.print(f"mode: {mode}")
                    time.sleep(0.5)
                    time.sleep(0.5)
            conf.previous_value = conf.rotate_step.value
        if not conf.rotate_button.value:
            print(f"MODE {mode}: rotary button pressed")
            time.sleep(0.5)
        if conf.btn15.value:
            print(f"MODE {mode}: button btn15 pressed")
#             conf.led.value = True
#             time.sleep(1)
#             conf.led.value = False
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn14.value:
            print(f"MODE {mode}: button btn14 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn13.value:
            print(f"MODE {mode}: button btn13 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn12.value:
            print(f"MODE {mode}: button btn12 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn11.value:
            print(f"MODE {mode}: button btn11 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn10.value:
            print(f"MODE {mode}: button btn10 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn9.value:
            print(f"MODE {mode}: button btn9 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn8.value:
            print(f"MODE {mode}: button btn8 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn7.value:
            print(f"MODE {mode}: button btn7 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn6.value:
            print(f"MODE {mode}: button btn6 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn5.value:
            print(f"MODE {mode}: button btn5 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn4.value:
            print(f"MODE {mode}: button btn4 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn3.value:
            print(f"MODE {mode}: button btn3 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn2.value:
            print(f"MODE {mode}: button btn2 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            keyboard.press(0xfb)
            conf.led.value = True
            time.sleep(0.1)
            conf.led.value = False
            keyboard.release(0xfb)
            0xf5
            time.sleep(0.5)
        if conf.btn1.value:
            print(f"MODE {mode}: button btn1 pressed")
            keyboard.press(MEDIA)
            conf.led.value = True
            time.sleep(0.5)
            conf.led.value = False
            keyboard.release(MEDIA)
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
        
        # if conf.btn5.value:
        #     print(f"button btn5 pressed")
        #     time.sleep(0.2)
        # if conf.btn4.value:
        #     print(f"button btn4 pressed")
        #     time.sleep(0.2)
        # if conf.btn3.value:
        #     print(f"button btn3 pressed")
        #     time.sleep(0.2)
        # if conf.btn2.value:
        #     print(f"button btn2 pressed")
        #     time.sleep(0.2)
        # if conf.btn1.value:
        #     print(f"button btn1 pressed")
        #     time.sleep(0.2)
        # if conf.btn0.value:
        #     print(f"button btn0 pressed")
        #     time.sleep(0.2)


key_detection()