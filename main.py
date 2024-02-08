#OpenCv and PCA9685 import
from __future__ import division
import cv2
import numpy as np
import Adafruit_PCA9685
import time
import imutils
from imutils import paths


pwm = Adafruit_PCA9685.PCA9685()
servo_min = 150  
servo_max = 600  

#Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

#Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#normal stand
def normal():
    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 440)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 240)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 280)
    time.sleep(0.01)


#move forward
def moveforward():
    #left feet
    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 240)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)

    pwm.set_pwm(0, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 100)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)

    #right feet
    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 220)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 350)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)

    pwm.set_pwm(0, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 100)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)

    pwm.set_pwm(0, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 100)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)


#kick the ball

def kick():
    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 440)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 240)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 280)
    time.sleep(0.01)

    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 350)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 440)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 340)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 280)
    time.sleep(0.01)

    time.sleep(2)

    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 600)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 440)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 240)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 280)
    time.sleep(0.01)

    time.sleep(2)

    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 350)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 440)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 340)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 280)
    time.sleep(0.01)

normal()

#setup
cap = cv2.VideoCapture(0)
qcd = cv2.QRCodeDetector()

#red colour
low_red = np.array([161,155,84])
upper_red = np.array([179,255,255])

#int cm
Known_distance = 20 #cm
Known_width = 4.5 #cm
#meed the red ball photo  

while True:
    def Focal_Length_Finder(Known_distance, real_width, width_in_rf_image):

        focal_length = (width_in_rf_image * Known_distance) / real_width
        return focal_length

    def obj_data(img):
        obj_width = 0
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv,low_red,upper_red)
        _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
        cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for c in cnts:
            x=600
            if cv2.contourArea(c)>x:
                x,y,w,h=cv2.boundingRect(c)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                obj_width = w
        return obj_width
    
    def Distance_finder(Focal_Length, Known_width, obj_width_in_frame):
        distance = (Known_width * Focal_Length)/obj_width_in_frame

        return distance    

    ref_image = cv2.imread("/home/haha/Pictures/redball.png")
    ref_image_obj_width = obj_data(ref_image)
    Focal_length_found = Focal_Length_Finder(Known_distance, Known_width, ref_image_obj_width)
    cv2.imshow("ref_image", ref_image)


    #print(Focal_length_found)
    
    #detect the ball from opencv

    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #red color 
    red_mask = cv2.inRange(hsv_frame,low_red,upper_red)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

    
        
    obj_width_in_frame=obj_data(frame)
    '''if obj_width_in_frame != 0:
        distanceofball = Distance_finder(Focal_length_found, Known_width, obj_width_in_frame)
        cv2.putText(frame, f"Distance: {round(distanceofball,2)} CM", (30, 35),cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 2)
    '''
    

    if obj_width_in_frame != 0:
        distanceofball2 = Distance_finder(Focal_length_found, Known_width, obj_width_in_frame)
        print(distanceofball2)
        
        #movement algorithm
        normal()
        if distanceofball2 > 20:
            moveforward()
            print("moving")
        else:
            kick()
            print("kicking")

                
    #the contour of ball
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        
        x_medium = int((x+x+w)/2)       
        cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        break
    
    
    
    
                
    cv2.imshow("Frame",frame)
    cv2.imshow("mask",red_mask)

    #exit key
    key = cv2.waitKey(1)
    if key == 27:
        break
  
    
cap.release()
cv2.destroyAllWindows()


            
