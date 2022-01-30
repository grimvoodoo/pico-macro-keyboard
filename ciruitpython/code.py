import conf
import time
import board
import busio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
# load the LCD library
import lcd
import i2c_pcf8574_interface

# Define vars
keyboard = Keyboard(usb_hid.devices)
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
iface = i2c_pcf8574_interface.I2CPCF8574Interface(i2c, 0x27)
mode = 1
last_position_left = None
last_position_right = None
start = True
screen_timeout = time.monotonic()
default_state = True
backlight_state = True

# key setup
shift = False
shift_time = None
ctrl = False
ctrl_time = None
alt = False
alt_time = None
led_time = None

# rotation encoder vars
rotate_drive_left = conf.rotate_drive_left
rotate_drive_right = conf.rotate_drive_right
rotate_step_left = conf.rotate_step_left
rotate_step_right = conf.rotate_step_right

# setup display
display = lcd.LCD(iface, num_rows=4, num_cols=20)
display.set_backlight(True)
display.set_display_enabled(True)


# Sets the screen back to default after a set time, and turns off the lcd backlight after a longer time
# also managed the modifier keys such as ctrl, shift and alt. it puts a half second sleep on them which refreshes
# every half a second, so I can hold the ctrl key and pass another which is used a lot in blender.
def sleep():
    global screen_timeout
    global default_state
    global backlight_state
    global shift_time
    global ctrl_time
    global alt_time
    global shift
    global alt
    global ctrl
    global led_time
    sleep_time = 10
    lights_out = 20
    if time.monotonic() > (screen_timeout + sleep_time) and default_state is False:
        mode_change()
        default_state = True
        screen_timeout = time.monotonic()
    elif time.monotonic() > (screen_timeout + lights_out):
        display.set_backlight(False)
        backlight_state = False

# the _time values are set to None by default and get set to `time.monotonic()` when the function is called.
# so the warning about expecting float but getting None can be ignored.
    if led_time is not None:
        if time.monotonic() > led_time + 0.5:
            conf.led.value = False
            led_time = None
    if shift_time is not None:
        if time.monotonic() > shift_time + 0.5:
            shift_time = None
            keyboard.release(Keycode.LEFT_SHIFT)
    if ctrl_time is not None:
        if time.monotonic() > ctrl_time + 0.5:
            ctrl_time = None
            keyboard.release(Keycode.LEFT_CONTROL)
    if alt_time is not None:
        if time.monotonic() > alt_time + 0.5:
            alt_time = None
            keyboard.release(Keycode.LEFT_ALT)


# prints the requested message to the lcd display
def lcd_display(message):
    global default_state
    global backlight_state
    if backlight_state is False:
        display.set_backlight(True)
    display.clear()
    display.print(message)
    default_state = False


# sets the mode and prints it to the LCD display
def mode_change():
    global mode
    keyboard.release_all()
    if mode == 1:
        lcd_display("Blender Model")
        display.set_cursor_pos(1, 0)
        display.print("Mode 1")
    elif mode == 2:
        lcd_display("Blender Sculpt")
        display.set_cursor_pos(1, 0)
        display.print("Mode 2")
    elif mode == 3:
        lcd_display("Krita Draw")
        display.set_cursor_pos(1, 0)
        display.print("Mode 3")


# Checks if the mode should be increased or decreased and passes the result to mode_change()
def mode_select(modifier):
    global mode
    if modifier == "up":
        if mode < 3:
            mode += 1
        else:
            mode = 1
    elif modifier == "down":
        if mode > 1:
            mode -= 1
        else:
            mode = 3
    mode_change()


def volume_select(modifier):
    global default_state
    if modifier == "up":
        lcd_display("Volume Up")
        keyboard.press(0x80)
        keyboard.release(0x80)
        default_state = False
        
    elif modifier == "down":
        lcd_display("Volume Down")
        keyboard.press(0x81)
        keyboard.release(0x81)
        default_state = False
    
    
# sets the reading from the left rotary dial and passes it to the mode_select()
def left_dial(position, direction):
    global last_position_left
    mode_count = 1
    if last_position_left is None:
        print("Initial setup")
        last_position_left = position
    elif position:
        if direction is not True:
            mode_select("up")
#             print("turned right")
            last_position_left = position
        else:
            mode_select("down")
#             print("turned left")
            last_position_left = position
    elif not position:
        if direction is True:
            mode_select("up")
#             print("turned right")
            last_position_left = position
        else:
            mode_select("down")
#             print("turned left")
            last_position_left = position


def right_dial(position, direction):
    global last_position_right
    mode_count = 1
    if last_position_right is None:
        last_position_right = position
    elif position:
        if direction is not True:
            volume_select("up")
#             print("turned right")
            last_position_right = position
        else:
            volume_select("down")
#             print("turned left")
            last_position_right = position
    elif not position:
        if direction is True:
            volume_select("up")
#             print("turned right")
            last_position_right = position
        else:
            volume_select("down")
#             print("turned left")
            last_position_right = position


def check_button(btn):
    global mode
    if mode == 1:
        key_list = conf.mode_1
    elif mode == 2:
        key_list = conf.mode_2
    elif mode == 3:
        key_list = conf.mode_3
    key_name = key_list[btn][0]
    print(f"key_name = {key_name}")
    key_press = key_list[btn][1]
    for key in key_press:
        keyboard.press(key)
    for key in key_press:
        keyboard.release(key)
    lcd_display(key_name)
#     keyboard.press(key_string)
#     keyboard.release(key_string)
    time.sleep(0.2)
    

def special_buttons(btn):
    global mode
    global shift
    global shift_time
    global ctrl
    global ctrl_time
    global alt
    global alt_time
    global led_time
    global backlight_state
    global screen_timeout
    screen_timeout = time.monotonic()
    if backlight_state is False:
        display.set_backlight(True)
    if mode == 1:
        key_list = conf.mode_1
    elif mode == 2:
        key_list = conf.mode_2
    elif mode == 3:
        key_list = conf.mode_3
    key = key_list[btn][0]
    if key is "SHIFT":
        shift = True
        keyboard.press(key_list[btn][1][0])
        shift_time = time.monotonic()
    elif key is "CTRL":
        ctrl = True
        ctrl_time = time.monotonic()
        keyboard.press(key_list[btn][1][0])
    elif key is "ALT":
        alt = True
        alt_time = time.monotonic()
        keyboard.press(key_list[btn][1][0])
    conf.led.value = True
    led_time = time.monotonic()


def run():
    global mode
    global previous_value
    global position_left
    global last_position_left
    global last_position_right
    global screen_timeout
    global default_state
    mode_change()
    time.sleep(0.5)

    while True:
        position_left = rotate_drive_left.value
        direction_left = rotate_step_left.value
        position_right = rotate_drive_right.value
        direction_right = rotate_step_right.value
        # left dial control
        if last_position_left is None or position_left != last_position_left:
            left_dial(position_left, direction_left)

        if last_position_right is None or position_right != last_position_right:
            right_dial(position_right, direction_right)
            
        if not conf.rotate_button1.value:
            lcd_display("rotary button 1")
            print(f"MODE {mode}: rotary button 1 pressed")
            time.sleep(0.2)
        if not conf.rotate_button2.value:
            lcd_display("Volume Muted")
            keyboard.press(0x7f)
            keyboard.release(0x7f)
            time.sleep(0.2)
            
        if conf.btn1.value:
            special_buttons("btn1")
        if conf.btn5.value:
            special_buttons("btn5")
        if conf.btn9.value:
            special_buttons("btn9")
            
        if conf.btn17.value:
            check_button("btn17")
        if conf.btn16.value:
            check_button("btn16")
        if conf.btn15.value:
            check_button("btn15")
        if conf.btn14.value:
            check_button("btn14")
        if conf.btn13.value:
            check_button("btn13")
        if conf.btn12.value:
            check_button("btn12")
        if conf.btn11.value:
            check_button("btn11")
        if conf.btn10.value:
            check_button("btn10")
        if conf.btn8.value:
            check_button("btn8")
        if conf.btn7.value:
            check_button("btn7")
        if conf.btn6.value:
            check_button("btn6")
        if conf.btn4.value:
            check_button("btn4")
        if conf.btn3.value:
            check_button("btn3")
        if conf.btn2.value:
            check_button("btn2")
        
        sleep()

run()