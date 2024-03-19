import cv2
import numpy as np
import Adafruit_PCA9685
import time
import imutils
from imutils import paths

class Robot:
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)
        self.servo_min = 150  
        self.servo_max = 600  
        self.cap = cv2.VideoCapture(0)
        self.qcd = cv2.QRCodeDetector()
        self.low_red = np.array([161,155,84])
        self.upper_red = np.array([179,255,255])
        self.Known_distance = 20 #cm
        self.Known_width = 4.5 #cm
        self.Focal_Length = 1

    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        pulse_length //= 4096     # 12 bits of resolution
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

    def Focal_Length_Finder(self, Known_distance, real_width, width_in_rf_image):
        focal_length = (width_in_rf_image * Known_distance) / real_width
        return focal_length

    def obj_data(self, img):
        obj_width = 100
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv,self.low_red,self.upper_red)
        _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
        cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for c in cnts:
            x=600
            if cv2.contourArea(c)>x:
                x,y,w,h=cv2.boundingRect(c)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                obj_width = w
        return obj_width

    def Distance_finder(self, Focal_Length, Known_width, obj_width_in_frame):
        distance = (Known_width * Focal_Length)/obj_width_in_frame
        return distance

    def track(self):
        ref_image = cv2.imread("/Volumes/MyPassport/Robot2/1111.jpg")
        ref_image_obj_width = self.obj_data(ref_image)
        Focal_length_found = self.Focal_Length_Finder(self.Known_distance, self.Known_width, ref_image_obj_width)
        while True:
            _, frame = self.cap.read()
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            red_mask = cv2.inRange(hsv_frame,self.low_red,self.upper_red)
            contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
            obj_width_in_frame=self.obj_data(frame)
            if obj_width_in_frame != 0:
                distanceofball = self.Distance_finder(Focal_length_found, self.Known_width, obj_width_in_frame)
                cv2.putText(frame, f"Distance: {round(distanceofball,2)} CM", (30, 35),cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 2)
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                x_medium = int((x+x+w)/2)       
                cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                obj_width_in_frame=self.obj_data(frame)
                break
            cv2.imshow("Frame",frame)
            cv2.imshow("mask",red_mask)
            key = cv2.waitKey(1)
            if key == 27:
                break
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    robot = Robot()
    robot.normal()
    robot.track()

if __name__ == "__main__":
    main()