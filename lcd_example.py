
from microbit import *
import microbit_i2c_lcd as lcd

i2c.init(sda=pin15,scl=pin13)

display = lcd.lcd(i2c)

display.lcd_display_string("micro:bit - 16x2", 1)
display.lcd_display_string("Hello World.", 2)

sleep(7500)

display.lcd_clear()
display.lcd_display_string("Goodbye.", 1)


i2c.init(sda=pin20,scl=pin19)
