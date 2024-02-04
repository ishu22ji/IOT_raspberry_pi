import RPi.GPIO as GP
import time
import random

GP.setmode(GP.BCM)
GP.setwarnings(False)
pins = [17, 22, 27, 5, 6, 13, 19]
GP.setup(pins, GP.OUT)

def blink_lights(duration):
    try:
        while True:
            random.shuffle(pins)
            for pin in pins:
                GP.output(pin, 1)
                time.sleep(duration)
                GP.output(pin, 0)
                time.sleep(duration)

    except KeyboardInterrupt:
        print("\nBlinking lights stopped by the user.")

    finally:
        GP.cleanup()
        print("GPIO cleanup completed. Exiting the program.")

try:
    print("\nRandom Blinking Lights: Activated!")
    user_duration = float(input("Enter the duration (in seconds) for each light state: "))
    blink_lights(user_duration)

except ValueError:
    print("Invalid input. Please enter a valid duration (in seconds).")

except KeyboardInterrupt:
    print("\nRandom blinking lights mode stopped by the user.")

finally:
    GP.cleanup()
    print("GPIO cleanup completed. Exiting the program.")
