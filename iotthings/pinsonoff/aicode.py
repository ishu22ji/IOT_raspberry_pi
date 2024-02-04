import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
GP.setwarnings(False)
GP.setup(17, GP.IN)
pins = [17, 22, 27, 5, 6, 13, 19]
GP.setup(pins, GP.OUT)

def debounce(pin):
    # A simple debounce function to stabilize the input reading
    stable_state = None
    for _ in range(5):
        if stable_state is None:
            stable_state = GP.input(pin)
        elif stable_state != GP.input(pin):
            return None
        time.sleep(0.01)
    return stable_state

try:
    while True:
        input_state = debounce(17)

        if input_state is None:
            continue

        if input_state == 0:  # Button pressed
            for i in range(len(pins)):
                GP.output(pins[i], 1)
                time.sleep(0.2)
            for r in range(len(pins)):
                time.sleep(0.2)
                GP.output(pins[r], 0)
        else:  # Button released
            GP.output(pins, 0)

except KeyboardInterrupt:
    print("\nProgram stopped by the user.")

finally:
    GP.cleanup()
    print("GPIO cleanup completed. Exiting the program.")
