import RPi.GPIO as GPIO
import time
import sys
from ADCDevice import *

class Controller:
  def __init__(self, zPin):
    self.adc = ADCDevice()
    findADC()
    
    self.zPin = zPin
    GPIO.setmode(GPIO.BOARD)        
    GPIO.setup(self.zPin,GPIO.IN,GPIO.PUD_UP)

  def findADC(self):
      if(self.adc.detectI2C(0x48)): # Detect the pcf8591.
        self.adc = PCF8591()
      elif(self.adc.detectI2C(0x4b)): # Detect the ads7830
        self.adc = ADS7830()
      else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        sys.exit()
       
  def getXValue(self):
    return self.adc.analogRead(1)
    
  def getYValue(self):
    return self.adc.analogRead(0)
    
  def getZValue(self):
    return GPIO.input(self.zPin)
  
  def destroy(self):
    self.adc.close()
    GPIO.cleanup()
    
  def __del__(self):
    self.destroy()
