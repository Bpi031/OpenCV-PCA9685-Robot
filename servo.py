import time
import Adafruit_PCA9685

class Robot:
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)

    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000
        pulse_length //= 60
        pulse *= 1000
        pulse //= pulse_length
        self.pwm.set_pwm(channel, 0, pulse)

    def move_servo(self, channel, pulse):
        self.pwm.set_pwm(channel, 0, pulse)
        time.sleep(0.01)

    def normal(self):
        positions = [320, 400, 500, 440, 120, 240, 200, 280]
        for i in range(8):
            self.move_servo(i, positions[i])

    def moveforward(self):
        # Define the positions for each step
        steps = [
            [320, 400, 500, 400, 120, 240, 200, 250],
            [280, 400, 500, 400, 100, 280, 300, 250],
            [320, 400, 500, 400, 220, 350, 200, 250],
            [280, 400, 500, 400, 100, 280, 300, 250]
        ]
        # Execute each step
        for step in steps:
            for i in range(8):
                self.move_servo(i, step[i])
            time.sleep(1)

    def kick(self):
        positions = [320, 400, 500, 440, 120, 240, 200, 280]
        for _ in range(2):
            for i in range(8):
                self.move_servo(i, positions[i])

def main():
    robot = Robot()
    print('press Ctrl-C to quit...')
    while True:
        robot.kick()

if __name__ == "__main__":
    main()