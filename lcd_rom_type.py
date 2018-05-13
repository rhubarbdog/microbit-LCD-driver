# requires RPi_I2C_driver.py
from microbit import *
import microbit_i2c_lcd as lcd

i2c.init(sda=pin15,scl=pin13)

display = lcd.lcd(i2c)

#
# this will print a pi symbol for ROM A00 japaneese
# print a divide symbol for the A02 ROM european

message = str(chr(247))+" is pi :Japan"
display.lcd_display_string(message, 1)
message = str(chr(247))+" is divide:Euro"
display.lcd_display_string(message, 2)


i2c.init(sda=pin20,scl=pin19)
