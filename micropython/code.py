import conf
import time
import digitalio
import rotaryio
import usb_hid



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



def key_detection():
    mode = 1
    # for x in pin_list:
    #     btn = button(x)
    while True:
        if conf.previous_value != conf.rotate_step.value:
            if not conf.rotate_step.value:
                if not conf.rotate_direction.value:
                    print("Rotated Right")
                    if mode < 3:
                        mode += 1
                    else:
                        mode = 1
                    time.sleep(0.5)
                else:
                    print("Rotated left")
                    if mode > 1:
                        mode -= 1
                    else:
                        mode = 3
                    time.sleep(0.5)
                    time.sleep(0.5)
            conf.previous_value = conf.rotate_step.value
        if not conf.rotate_button.value:
            print(f"MODE {mode}: rotary button pressed")
            time.sleep(0.5)
        if conf.btn15.value:
            print(f"MODE {mode}: button GP15 pressed")
            conf.led.value = True
            time.sleep(1)
            conf.led.value = False
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn14.value:
            print(f"MODE {mode}: button GP14 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn13.value:
            print(f"MODE {mode}: button GP13 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn12.value:
            print(f"MODE {mode}: button GP12 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn11.value:
            print(f"MODE {mode}: button GP11 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn10.value:
            print(f"MODE {mode}: button GP10 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn9.value:
            print(f"MODE {mode}: button GP9 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn8.value:
            print(f"MODE {mode}: button GP8 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn7.value:
            print(f"MODE {mode}: button GP7 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        if conf.btn6.value:
            print(f"MODE {mode}: button GP6 pressed")
            # if mode == 1:
            # elif mode == 2:
            # elif mode == 3:
            time.sleep(0.5)
        # if conf.btn5.value:
        #     print(f"button GP5 pressed")
        #     time.sleep(0.2)
        # if conf.btn4.value:
        #     print(f"button GP4 pressed")
        #     time.sleep(0.2)
        # if conf.btn3.value:
        #     print(f"button GP3 pressed")
        #     time.sleep(0.2)
        # if conf.btn2.value:
        #     print(f"button GP2 pressed")
        #     time.sleep(0.2)
        # if conf.btn1.value:
        #     print(f"button GP1 pressed")
        #     time.sleep(0.2)
        # if conf.btn0.value:
        #     print(f"button GP0 pressed")
        #     time.sleep(0.2)


key_detection()
