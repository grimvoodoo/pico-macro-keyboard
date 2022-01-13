import time
import digitalio
import board
import conf

exclusions = set(list(["_", "GP0", "GP28_A2"]))
board_list = set(list(dir(board)))
pin_list = ["GP15", "GP14"]

# filters out the bad entries from the GPIO pins
# for x in board_list:
#     for y in exclusions:
#         if y in x:
#             break
#         else:
#             pin_list.append(x)


def button(key):
    btn_pin = getattr(board, key)
    btn = digitalio.DigitalInOut(btn_pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    return btn


def key_detection():
    # for x in pin_list:
    #     btn = button(x)
    while True:
        if conf.btn15.value:
            print(f"button GP15 pressed")
            time.sleep(0.2)
        if conf.btn14.value:
            print(f"button GP14 pressed")
            time.sleep(0.2)


# btn1_pin = board.GP15
# btn1 = digitalio.DigitalInOut(btn1_pin)
# btn1.direction = digitalio.Direction.INPUT
# btn1.pull = digitalio.Pull.DOWN


# def button_pressed():
#     print(board.board_id)
#     print(digitalio.DigitalInOut.value)
    # print(button["gpio"])
    # while True:
    #     if pin:
    #         print(f"{btn} pressed")
    #     time.sleep(0.1)


# button_pressed()
# for gp in button:
#     pin = getattr(board, gp)
#     btn = digitalio.DigitalInOut(pin)
#     btn.direction = digitalio.Direction.INPUT
#     btn.pull = digitalio.Pull.DOWN
#     while True:
#         if btn.value:
#             print(f"{gp} pressed")
#             time.sleep(0.1)


# btn1_pin = board.GP15
# btn1 = digitalio.DigitalInOut(btn1_pin)
# btn1.direction = digitalio.Direction.INPUT
# btn1.pull = digitalio.Pull.DOWN
#
# btn2_pin = board.GP14
# btn2 = digitalio.DigitalInOut(btn2_pin)
# btn2.direction = digitalio.Direction.INPUT
# btn2.pull = digitalio.Pull.DOWN

# while True:
#     if btn1.value:
#         print("button 1 pressed")
#     time.sleep(0.1)
#
#     if btn2.value:
#         print("button 2 pressed")
#     time.sleep(0.1)


key_detection()
