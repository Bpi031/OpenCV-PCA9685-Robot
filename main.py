import cv2
import numpy as np
import Adafruit_PCA9685
import time

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
        for i in range(8):
            self.move_servo(i, 320)

    def moveforward(self):
        for i in range(8):
            self.move_servo(i, 280)

    def kick(self):
        for i in range(8):
            self.move_servo(i, 300)

class OpenCVOperations:
    def __init__(self):
        self.low_red = np.array([161,155,84])
        self.upper_red = np.array([179,255,255])

    def Focal_Length_Finder(self, Known_distance, real_width, width_in_rf_image):
        focal_length = (width_in_rf_image * Known_distance) / real_width
        return focal_length

    def obj_data(self, img):
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv,self.low_red,self.upper_red)
        _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
        cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for c in cnts:
            if cv2.contourArea(c)>600:
                x,y,w,h=cv2.boundingRect(c)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                return w
        return 0

    def Distance_finder(self, Focal_Length, Known_width, obj_width_in_frame):
        distance = (Known_width * Focal_Length)/obj_width_in_frame
        return distance
    

def main():
    robot = Robot()
    cv_operations = OpenCVOperations()

    cap = cv2.VideoCapture(0)
    Known_distance = 20
    Known_width = 4.5
    ref_image = cv2.imread("/home/haha/Pictures/redball.png")
    ref_image_obj_width = cv_operations.obj_data(ref_image)
    Focal_length_found = cv_operations.Focal_Length_Finder(Known_distance, Known_width, ref_image_obj_width)

    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        red_mask = cv2.inRange(hsv_frame,cv_operations.low_red,cv_operations.upper_red)
        contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
        obj_width_in_frame=cv_operations.obj_data(frame)

        if obj_width_in_frame != 0:
            distanceofball2 = cv_operations.Distance_finder(Focal_length_found, Known_width, obj_width_in_frame)
            print(distanceofball2)
            robot.normal()
            if distanceofball2 > 20:
                robot.moveforward()
                print("moving")
            else:
                robot.kick()
                print("kicking")

        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            x_medium = int((x+x+w)/2)       
            cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            break

        cv2.imshow("Frame",frame)
        cv2.imshow("mask",red_mask)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()