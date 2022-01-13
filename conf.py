import board
import digitalio


def button(key):
    btn_pin = getattr(board, key)
    btn = digitalio.DigitalInOut(btn_pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    return btn


btn1 = button("GP1")
btn2 = button("GP2")
btn3 = button("GP3")
btn4 = button("GP4")
btn5 = button("GP5")
btn6 = button("GP6")
btn7 = button("GP7")
btn8 = button("GP8")
btn9 = button("GP9")
btn10 = button("GP10")
btn11 = button("GP11")
btn12 = button("GP12")
btn13 = button("GP13")
btn14 = button("GP14")
btn15 = button("GP15")
