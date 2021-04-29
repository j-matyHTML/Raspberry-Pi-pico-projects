from machine import Pin, Timer
import urandom

#Define onboard LED
led = Pin(25, Pin.OUT)
LED_state = True
tim = Timer()

#Select random frequency and print it
random_number = urandom.uniform(1, 35)
print (random_number)

#Set the timer
def tick(timer):
    global led, LED_state
    LED_state = not LED_state
    led.value(LED_state)

tim.init(freq=random_number, mode=Timer.PERIODIC, callback=tick)
