import board
import digitalio
import rotaryio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import board
import busio

previous_value = True


def rotary_encoder(key):
    btn_pin = getattr(board, key)
    btn = digitalio.DigitalInOut(btn_pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    return btn


def button(key):
    btn_pin = getattr(board, key)
    btn = digitalio.DigitalInOut(btn_pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    return btn


rotate_button = digitalio.DigitalInOut(board.GP18)
rotate_button.direction = digitalio.Direction.INPUT
rotate_button.pull = digitalio.Pull.UP
lastPosition = 0


led = digitalio.DigitalInOut(board.GP20)
led.direction = digitalio.Direction.OUTPUT
btn1 = button("GP2")
btn2 = button("GP3")
btn3 = button("GP4")
btn4 = button("GP5")
btn5 = button("GP6")
btn6 = button("GP7")
btn7 = button("GP8")
btn8 = button("GP9")
btn9 = button("GP10")
btn10 = button("GP11")
btn11 = button("GP12")
btn12 = button("GP13")
btn13 = button("GP14")
btn14 = button("GP26")
btn15 = button("GP27")
rotate_direction = rotary_encoder("GP16")
rotate_step = rotary_encoder("GP17")
# btn18 = button("GP18")
# btn13 = rotary_encoder("GP13")
# dirPin = rotary_encoder("GP14")
# stepPin = rotary_encoder("GP15")