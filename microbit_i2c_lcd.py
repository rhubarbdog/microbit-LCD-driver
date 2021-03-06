# This code began life as an Arduino driver in the public domain
# It was initially converted by a now unknown man from Amazon
# Credit for this code goes to "natbett" of the Raspberry Pi Forum 18/02/13
# https://www.raspberrypi.org/forums/viewtopic.php?t=34261&p=378524

# Before running this code make sure to run i2c detect
# and match the LCD address of your device

# converted to microbit by Phil Hall

from microbit import *
import time

# LCD Address, could be  0x27
ADDRESS = 0x3f
# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80
# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00
# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00
# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00
# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00
# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00
En = 0b00000100 # Enable bit
Rw = 0b00000010 # Read/Write bit
Rs = 0b00000001 # Register select bit

class i2c_device:
   def __init__(self, bus, addr):
      self.__addr = addr
      self.__bus = bus
# Write a single command
   def write_cmd(self, cmd):
      buf=bytearray(1)
      buf[0]=cmd
      self.__bus.write(self.__addr,buf)
      time.sleep_us(100)
      
class lcd:
   #initializes objects and lcd
   def __init__(self,bus=None):
      self.__lcd_device = i2c_device(bus,ADDRESS)
      self._lcd_write(0x03)
      self._lcd_write(0x03)
      self._lcd_write(0x03)
      self._lcd_write(0x02)
      self._lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
      self._lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
      self._lcd_write(LCD_CLEARDISPLAY)
      self._lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
      time.sleep_ms(200)
   # clocks EN to latch command
   def _lcd_strobe(self, data):
      self.__lcd_device.write_cmd(data | En | LCD_BACKLIGHT)
      time.sleep_us(500)
      self.__lcd_device.write_cmd(((data & ~En) | LCD_BACKLIGHT))
      time.sleep_us(100)
   def _lcd_write_four_bits(self, data):
      self.__lcd_device.write_cmd(data | LCD_BACKLIGHT)
      self._lcd_strobe(data)
   # write a command to lcd
   def _lcd_write(self, cmd, mode=0):
      self._lcd_write_four_bits(mode | (cmd & 0xF0))
      self._lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))
   # put string function
   def lcd_display_string(self, string, line):
      if line == 1:
         self._lcd_write(0x80)
      if line == 2:
         self._lcd_write(0xC0)
      if line == 3:
         self._lcd_write(0x94)
      if line == 4:
         self._lcd_write(0xD4)
      for char in string:
         self._lcd_write(ord(char), Rs)
   # clear lcd and set to home
   def lcd_clear(self):
      self._lcd_write(LCD_CLEARDISPLAY)
      self._lcd_write(LCD_RETURNHOME)
