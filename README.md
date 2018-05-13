# microbit-LCD-driver
An i2c driver for 16x2 .. 40x4 LCD displays on the microbit

The module microbit_i2c_lcd.py uses the module time. That requires a modern firmware, version 1.9.2 works.  If you only have vanilla firmware (version 1.7.9) available you can swap all time.sleep_ms for microbit's sleep and swap time.sleep_us for microbits sleep of 1 milli second. This will degrade the writing to speed.

These LCD displays run on 5v not the 3v you can get from the microbit edge connector.  You need a separate power suply, remember you need to connect all grounds together.  I2C protocol requires that the data line (SDA) and the clock (SCL) line have pull up resistors in a range of 3K-10K. I have pulled them to the microbit's 3v and everything works.

My breakout board doesn't have pins 19 and 20 which are the microbit's i2c pins. So both lcd_example.py and lcd_rom_type.py use function i2c.init. This requires a modern firmware, version 1.9.2 works.

lcd_rom_type.py is used to determine if you have a japanese or european character set.
