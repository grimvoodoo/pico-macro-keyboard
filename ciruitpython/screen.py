#
# Metronome Maker Pi Pico, programmed with CircuitPython
#
# Reference:
# - https://learn.adafruit.com/metronome-clue
#
# Tutorial
# - https://tutorial.cytron.io/
#
# Raspberry Pi Pico
# - Maker Pi Pico https://my.cytron.io/p-maker-pi-pico?tracking=idris
# - Grove 16x2 LCD https://my.cytron.io/p-grove-16-x-2-lcd-white-on-blue?tracking=idris
#
# Additional Libraries
# - simpleio.mpy
# - neopixel.mpy
# Download CircuitPython Libraries Bundle - https://circuitpython.org/libraries
#
# Update:
# 3 Aug 2021 - Tested with CircuitPython Pico 6.3.0
#

import time
import board
import digitalio
import simpleio
import neopixel
import busio
from grove_lcd_i2c import Grove_LCD_I2C

button1 = digitalio.DigitalInOut(board.GP2)
button1.direction = digitalio.Direction.INPUT

button2 = digitalio.DigitalInOut(board.GP3)
button2.direction = digitalio.Direction.INPUT

button3 = digitalio.DigitalInOut(board.GP4)
button3.direction = digitalio.Direction.INPUT

NONE = (0, 0, 0)
RED = (100, 0, 0)
GREEN = (0, 100, 0)
pixels = neopixel.NeoPixel(board.GP28, 1)
pixels[0] = NONE

LCD_SDA = board.GP0
LCD_SCL = board.GP1
LCD_ADDR = 0x27
i2c = busio.I2C(scl=LCD_SCL, sda=LCD_SDA)
lcd = Grove_LCD_I2C(i2c, LCD_ADDR)

lcd.home()
lcd.print("Metronome on\nMaker Pi Pico")

tempo = 120  # in bpm
print("BPM: {}".format(tempo))
time_signature = 4  # Beats per measure
BEEP_DURATION = 0.05
delay = 60 / tempo

def metronome(accent):  # Play metronome sound and flash display
    if accent == 1:  # Put emphasis on downbeat
        pixels[0] = GREEN
        simpleio.tone(board.GP18, 1800, BEEP_DURATION)
    else:
        pixels[0] = RED
        simpleio.tone(board.GP18, 1200, BEEP_DURATION)
    pixels[0] = NONE

time.sleep(0.2)
tempo_increment = 1  # increment for tempo value setting
feedback_mode = 0  # 0 is sound and visual, 1 is sound only, 2 is visual only
running = True
beat = 1

time.sleep(2)

lcd.cursor_position(0, 0)
lcd.print("Tempo: {}   \nTSign: {}/4   ".format(tempo, time_signature))

t0 = time.monotonic()  # set start time

while True:

    if button1.value == False: # Button 1 is pressed
        if tempo > 40:
            tempo = tempo - tempo_increment
            delay = 60 / tempo
            lcd.cursor_position(0, 0)
            lcd.print("Tempo: {}   \nTSign: {}/4   ".format(tempo, time_signature))
            time.sleep(0.2)  # debounce

    elif button2.value == False: # Button 2 is pressed
        if tempo < 330:
            tempo = tempo + tempo_increment
            delay = 60 / tempo
            lcd.cursor_position(0, 0)
            lcd.print("Tempo: {}   \nTSign: {}/4   ".format(tempo, time_signature))
            time.sleep(0.2)  # debounce

    elif button3.value == False: # Button 3 is pressed
        print("sig change")
        if time_signature == 4:
            time_signature = 3
        else:
            time_signature = 4
        lcd.cursor_position(0, 0)
        lcd.print("Tempo: {}   \nTSign: {}/4   ".format(tempo, time_signature))
        time.sleep(0.4)
        beat = 1  # start with downbeat

    elif time.monotonic() - t0 >= delay:
        t0 = time.monotonic()  # reset time before click to maintain accuracy
        metronome(beat)
        beat = beat - 1
        if beat == 0:  # if the downbeat was just played, start at top of measure
            beat = time_signature