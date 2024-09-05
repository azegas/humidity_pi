import RPi.GPIO as GPIO
import time

# Set up GPIO using BOARD numbering
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin connected to the LED
LED_PIN = 12  # This is physical pin 12, which corresponds to GPIO18 in BCM mode

# Set up the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Turn the LED on
    print("Turning LED on")
    GPIO.output(LED_PIN, GPIO.HIGH)

    # Check the voltage being sent to the LED
    voltage = GPIO.input(LED_PIN) * 3.3
    print(f"The LED is receiving approximately {voltage:.1f} volts")
    
    # Wait for 2 seconds
    time.sleep(2)
    
    # Turn the LED off
    print("Turning LED off")
    GPIO.output(LED_PIN, GPIO.LOW)
    
    # Wait for 2 seconds
    time.sleep(2)

finally:
    # Clean up GPIO on exit
    GPIO.cleanup()

print("LED control complete")
