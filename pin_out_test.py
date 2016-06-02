# PWM attempt 1

import wiringpi
import time


case = 3

if case == 1:
	wiringpi.wiringPiSetup()
	pins = [0,1,2,3]
elif case == 2:
	wiringpi.wiringPiSetupPhys()
	pins = [11,12,13,15]
elif case == 3:
	wiringpi.wiringPiSetupGpio()
	pins = [17,18,27,22]
	
print('case = %i' % case)
print('pins = %s' % pins)

for i, pin in enumerate(pins):
	wiringpi.pinMode(pin, 1) # sets GPIO 24 to output 
	for j in range(i+1):
		wiringpi.digitalWrite(pin, 1)
		time.sleep(0.5)
		wiringpi.digitalWrite(pin, 0)
		time.sleep(0.5)

