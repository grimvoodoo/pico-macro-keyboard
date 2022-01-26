import board
import digitalio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import busio
from adafruit_hid.keycode import Keycode


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

# rotation_encoder buttons have to be up by default
rotate_button1 = digitalio.DigitalInOut(board.GP18)
rotate_button1.direction = digitalio.Direction.INPUT
rotate_button1.pull = digitalio.Pull.UP

rotate_button2 = digitalio.DigitalInOut(board.GP21)
rotate_button2.direction = digitalio.Direction.INPUT
rotate_button2.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.GP22)
led.direction = digitalio.Direction.OUTPUT

# This is the sequence I wired up the controler in, it will vary depending on how you wire it up.
btn1 = button("GP6")
btn2 = button("GP9")
btn3 = button("GP12")
btn4 = button("GP15")
btn5 = button("GP5")
btn6 = button("GP8")
btn7 = button("GP11")
btn8 = button("GP14")
btn9 = button("GP4")
btn10 = button("GP7")
btn11 = button("GP10")
btn12 = button("GP13")
btn13 = button("GP28")
btn14 = button("GP2")
btn15 = button("GP27")
btn16 = button("GP26")
btn17 = button("GP3")

rotate_drive_left = rotary_encoder("GP16")
rotate_step_left = rotary_encoder("GP17")
rotate_drive_right = rotary_encoder("GP19")
rotate_step_right = rotary_encoder("GP20")

# mode_1 = {
#     "btn1": ["CTRL", [Keycode.LEFT_CONTROL]],
#     "btn2": ["X", [Keycode.X]],
#     "btn3": ["Y", [Keycode.Y]],
#     "btn4": ["Z", [Keycode.Z]],
#     "btn5": ["SHIFT", [Keycode.LEFT_SHIFT]],
#     "btn6": ["G", [Keycode.G]],
#     "btn7": ["S", [Keycode.S]],
#     "btn8": ["R", [Keycode.R]],
#     "btn9": ["ALT", [Keycode.LEFT_ALT]],
#     "btn10": ["A", [Keycode.A]],
#     "btn11": ["M", [Keycode.M]],
#     "btn12": ["F", [Keycode.F]],
#     "btn13": ["CTRL + Z", [Keycode.LEFT_CONTROL, Keycode.Z]],
#     "btn14": ["Skip Back", [0xea]],
#     "btn15": ["Play/Pause", [0xe8]],
#     "btn16": ["Spotify", [0x69]],
#     "btn17": ["Skip Forward", [0xeb]],
# }

mode_1 = {
    "btn1": ["CTRL", Keycode.LEFT_CONTROL],
    "btn2": ["X", Keycode.X],
    "btn3": ["Y", Keycode.Y],
    "btn4": ["Z", Keycode.Z],
    "btn5": ["SHIFT", Keycode.LEFT_SHIFT],
    "btn6": ["G", Keycode.G],
    "btn7": ["S", Keycode.S],
    "btn8": ["R", Keycode.R],
    "btn9": ["ALT", Keycode.LEFT_ALT],
    "btn10": ["A", Keycode.A],
    "btn11": ["M", Keycode.M],
    "btn12": ["F", Keycode.F],
    "btn13": ["CTRL + Z", f"{Keycode.LEFT_CONTROL}, {Keycode.Z}"],
    "btn14": ["Skip Back", 0xea],
    "btn15": ["Play/Pause", 0xe8],
    "btn16": ["Spotify", 0x69],
    "btn17": ["Skip Forward", 0xeb],
}

mode_2 = {
    "btn1": ["CTRL", Keycode.LEFT_CONTROL],
    "btn2": ["X", Keycode.KEYPAD_ONE],
    "btn3": ["Y", Keycode.KEYPAD_TWO],
    "btn4": ["Z", Keycode.KEYPAD_THREE],
    "btn5": ["SHIFT", Keycode.LEFT_SHIFT],
    "btn6": ["G", Keycode.G],
    "btn7": ["S", Keycode.S],
    "btn8": ["R", Keycode.R],
    "btn9": ["ALT", Keycode.LEFT_ALT],
    "btn10": ["A", Keycode.A],
    "btn11": ["M", Keycode.M],
    "btn12": ["F", Keycode.F],
    "btn13": ["CTRL + Z", 0x7a],
    "btn14": ["Skip Back", 0xea],
    "btn15": ["Play/Pause", 0xe8],
    "btn16": ["Spotify", 0x68],
    "btn17": ["Skip Forward", 0xeb],
}

mode_3 = {
    "btn1": ["CTRL", Keycode.LEFT_CONTROL],
    "btn2": ["X", Keycode.X],
    "btn3": ["Y", Keycode.Y],
    "btn4": ["Z", Keycode.Z],
    "btn5": ["SHIFT", Keycode.LEFT_SHIFT],
    "btn6": ["G", Keycode.G],
    "btn7": ["S", Keycode.S],
    "btn8": ["R", Keycode.R],
    "btn9": ["ALT", Keycode.LEFT_ALT],
    "btn10": ["A", Keycode.A],
    "btn11": ["M", Keycode.M],
    "btn12": ["F", Keycode.F],
    "btn13": ["CTRL + Z", f"{Keycode.LEFT_CONTROL}, {Keycode.Z}"],
    "btn14": ["Skip Back", 0xea],
    "btn15": ["Play/Pause", 0xe8],
    "btn16": ["Spotify", 0x69],
    "btn17": ["Skip Forward", 0xeb],
}


