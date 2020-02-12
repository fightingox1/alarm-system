# source for keypad info https://tutorials-raspberrypi.com/connecz-raspberry-pi-kecpad-code-lock/
# keypad 1 https://www.amazon.com/-/es/FlashTree-Teclado-Arduino-unidades-Matrix/dp/B07VZV1H42/ref=sr_1_8?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=matrix+keypad+3-4&qid=1581519536&sr=8-8 
# keypad 2 https://www.amazon.com/Numeric-Sunreed-Portable-Desktop-Computer/dp/B01N9SUH9Z/ref=asc_df_B01N9SUH9Z/?tag=hyprod-20&linkCode=df0&hvadid=312727440900&hvpos=1o8&hvnetw=g&hvrand=9255476657117458018&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9008471&hvtargid=pla-584104056123&psc=1
#gpio 24 pin 18 and gpio 22 pin 15 are for alarm
import time
import RPi.GPIO as GPIO
from keypad import keypad
 
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
while True:
         button_state = GPIO.input(23)
         while button_state == False:
          if __name__ == '__main__':
              # Initialize
              kp = keypad(columnCount = 3)
              # waiting for a keypress
              digit = None
              while digit == None:
                  digit = kp.getKey()
              # Print result
              print digit
              time.sleep(0.5)
              ###### 4 Digit wait ######
              seq = []
              for i in range(4):
                  digit = None
                  while digit == None:
                      digit = kp.getKey()
                  seq.append(digit)
                  time.sleep(0.4)
              # Check digit code
              print(seq)
              if seq == [1, 2, 3, '#']:
                  print "Code accepted"
              else:
                from playsound import playsound
                playsound('audio.mp3')
         else:
          from playsound import playsound
          playsound('audio.mp3')
