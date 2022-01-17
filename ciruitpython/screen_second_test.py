# lcd_display_demo.py

# Raspberry Pi Pico - LCD I2C 20x4 Character Display demo

# Display text on a 20x4 character display using an I2C interface.
# IDeATe stocks a small quantity of these devices in the Hunt A10 Physical
# Computing Lab as part 0627.

# This is a generic display part which uses a PCF8574 "Remote 8-Bit I/O Expander
# for I2C Bus" to drive the LCD display parallel port.  The default I2C address
# is 0x27 as determined by a bus scan.

#---- LCD library ---------------------------------------------------------
# This sample uses a third-party library which is not included in the firmware,
# but which must be copied to the board.
#
# PCF8574 LCD library: https://github.com/dhalbert/CircuitPython_LCD
#
# To install, clone the repo or download it, then copy the lcd/ folder
# to the lib/ folder on the CIRCUITPY device.

#---- electrical connections ---------------------------------------------------
# The Pico has two hardware I2C ports which can each be mapped to a number of
# possible pin pairs.  This example uses pins 6 and 7 for I2C0 SDA
# and SCL.  For alternate choices please see the official pinout diagram.

# Pico                  display         description
# pin 7/GP5/I2C0 SCL    SCL             I2C clock from port 0
# pin 6/GP4/I2C0 SDA    SDA             I2C data from port 0
# pin 36/3.3VOUT        VCC             3.3V to power display
# pin 38/GND            GND             common ground

# On the display, install a jumper on the two-pin header labeled LED in order to
# power the backlight, otherwise the display is almost unreadable.

################################################################
# related CircuitPython module documentation:

# board  https://circuitpython.readthedocs.io/en/latest/shared-bindings/board/index.html
# busio  https://circuitpython.readthedocs.io/en/latest/shared-bindings/busio/index.html
# time   https://circuitpython.readthedocs.io/en/latest/shared-bindings/time/index.html

################################################################################
# load standard Python modules
import time

# load the CircuitPython hardware definition module for pin definitions
import board

# load the CircuitPython I2C support
import busio

# load the LCD library
import lcd
import i2c_pcf8574_interface

#---------------------------------------------------------------
# The device is connected to I2C0 on pins 6 and 7.
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)

iface = i2c_pcf8574_interface.I2CPCF8574Interface(i2c, 0x27)
display = lcd.LCD(iface, num_rows=4, num_cols=20)
display.set_backlight(True)
display.set_display_enabled(True)

display.print("Hello, world.")

#---------------------------------------------------------------
# Run the main loop to generate a counting display.

while True:
    for count in range(10000):
        display.set_cursor_pos(1, 4)
        display.print("%04d" % count)
        print("%04d" % count)
        time.sleep(1)
        