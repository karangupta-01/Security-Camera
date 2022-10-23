Hello!

This is a security camera which takes pictures from your web-camera and it also take screen shot of your screen in intervals which is set by the user. The program will start as soon as you have login in your system but it will only take pictures and screen shots when a specific application is opened.

You need to download the files and save them in a directory called "Security Camera".

Save the start.bat file in "C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" location. Replace User with your own User's name. 
Edit the start.bat file and replace K:\Security Camera with the complete path of your directory where you have stored your Security Camera.py file.

You should check your camera port if you get an error regarding the image capture and replace it in the Security Camera.py Line 16.

In line 9 you can change the time interval in which the program works by changing the numeric value.

In line 46 you need to input the name of the application you want to use as the starting key for your Security Camera. You have to input the name of the application with ".exe".


Download the below mentioned modules for the program to work:

a) cv2
    pip install opencv-python

b) numpy
    pip install numpy

c) pyautogui
    pip install pyautogui

d) wmi
    pip install wmi