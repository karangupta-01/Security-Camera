import cv2
import numpy as np
import pyautogui
import wmi
import time

f = wmi.WMI() # Initializing the wmi constructor
time.sleep(20)
TIME = 2 
def main():
    a = 0
    while(True):
        time.sleep(TIME)
        # global a
        def img_capture():
            cam_port = 0  # Here "0" indicates the port in which your web-camera is plugged. 
                        # Change its value according to the port in which your web-camera is plugged.
            cam = cv2.VideoCapture(cam_port)   # Captures the image
            result, image = cam.read()    # Read the image

            if result:
                cv2.imshow("img", image)      # showing result, it take frame name and image output 
                cv2.imwrite(f"img{a}.png", image) # saving image in local storage
                cv2.destroyWindow("img")  # If keyboard interrupt occurs, destroy image window
            else:
                print("No image detected please try again.")

        def ss_capture():
            # take screenshot using pyautogui
            image = pyautogui.screenshot()

            # since the pyautogui takes as a PIL(pillow) and in RGB we need to
            # convert it to numpy array and BGR so we can write it to the disk
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            # writing it to the disk using opencv
            cv2.imwrite(f"ss{a}.png", image)
        
        a += 1
        img_capture()
        ss_capture()


# Iterating through all the running processes
for process in f.Win32_Process():
    if ".exe" in process.Name:		
	    main()