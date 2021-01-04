#pilow module is used to take screenshots 
#it works only on windows and mac
#in pilow ImageGrab is the class used to take screenshot


#here is the program demo to show working of pilow module and its class ImageGrab

#1: import required module here Pilow is the module and it is written as PIL 
import PIL.ImageGrab 
#note> while importing module the class used in it is also called together

import PIL.ImageGrab as demo
#compressing such a big line command into one word (demo) so complexity is reduced

import os
#os module is also imported for the purpose of saving screen shot in desired location

import getpass
#getpass is the module which gets the user name of the particular system

b=getpass.getuser()
a="c:\\Users\\"
c="\\Desktop"
d=a+b+c
s=os.chdir(d)


capture=demo.grab(s)
#take screenshot where demo is code shortend as demo and capture is field declared
#.grab is the function which takes picture

capture.save("screenshot.png","png")
#it saves the screenshot take with the name given here ar.png and the format type is png

capture.show() 
#shows the picture taken by the above code

