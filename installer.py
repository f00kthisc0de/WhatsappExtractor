#!/bin/python3

from os import system as command 
from termcolor import colored as c

print(c('''

 _              _          _  _             
(_)            | |        | || |            
 _  _ __   ___ | |_  __ _ | || |  ___  _ __ 
| || '_ \ / __|| __|/ _` || || | / _ \| '__|
| || | | |\__ \| |_| (_| || || ||  __/| |   
|_||_| |_||___/ \__|\__,_||_||_| \___||_|   
                                            
''','green','on_grey',['bold']))


print(c("Installing ADB and pip modules","green"))
command("sudo apt-get install adb; pip3 install termcolor")
print(c("Sucess!!!!","green"))