import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

mode_dict = {1: blender - modeling,
             2: blender - sculpting,
             3: krita - drawing}
btn_dict = {1: }


mode1 = {
    1: keyboard.press(Keycode.SHIFT),
    2: keyboard.press(Keycode.X),
    3: keyboard.press(Keycode.Y),
    4: keyboard.press(Keycode.Z),
    5: keyboard.press(Keycode.CONTROL),
    6: keyboard.press(Keycode.G),
    7: keyboard.press(Keycode.S),
    8: keyboard.press(Keycode.R),
    9: keyboard.press(Keycode.ALT),
    10: keyboard.press(Keycode.A),
    11: keyboard.press(Keycode.B),
    12: keyboard.press(Keycode.M),
    13: keyboard.press(Keycode.CONTROL, keycode.Z),
    14: keyboard.press(0xea),
    15: keyboard.press(0xe8),
    16: keyboard.press(),
    17: keyboard.press(0xeb)
}

#define KEY_MEDIA_PLAYPAUSE 0xe8
#define KEY_MEDIA_STOPCD 0xe9
#define KEY_MEDIA_PREVIOUSSONG 0xea
#define KEY_MEDIA_NEXTSONG 0xeb
#define KEY_MEDIA_VOLUMEUP 0xed
#define KEY_MEDIA_VOLUMEDOWN 0xee
#define KEY_MEDIA_MUTE 0xef

# key layout
# 14  15  16  17
#       LDC
#
#       13
# 9   10  11  12
# 5   6   7   8
# 1   2   3   4