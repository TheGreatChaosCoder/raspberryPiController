import RPi.GPIO as GPIO

class Button:
  def __init__(self, pin):
    self.pin = pin
  
    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode
    
  def getButtonPress(self):
    return False if GPIO.input(buttonPin)==GPIO.LOW else True
    
  def destroy(self):
    GPIO.cleanup()
    
  def __del__(self):
    self.destroy()
