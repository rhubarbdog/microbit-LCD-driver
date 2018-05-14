from microbit import *
import microbit_i2c_lcd as lcd

i2c.init(sda=pin15,scl=pin13)

display = lcd.lcd(i2c)

display.lcd_display_string(str(chr(247)), 1)
print("this will display a pi symbol for ROM A00 japaneese\n"+\
      "display a divide symbol for the A02 ROM european")

i2c.init(sda=pin20,scl=pin19)
