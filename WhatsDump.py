#!/bin/python3

from os import system as command 
from termcolor import colored as c

def menue():

    print(c('''

 __       __  __                    __                                                   
/  |  _  /  |/  |                  /  |                                                  
$$ | / \ $$ |$$ |____    ______   _$$ |_    _______   ______    ______    ______         
$$ |/$  \$$ |$$      \  /      \ / $$   |  /       | /      \  /      \  /      \        
$$ /$$$  $$ |$$$$$$$  | $$$$$$  |$$$$$$/  /$$$$$$$/  $$$$$$  |/$$$$$$  |/$$$$$$  |       
$$ $$/$$ $$ |$$ |  $$ | /    $$ |  $$ | __$$      \  /    $$ |$$ |  $$ |$$ |  $$ |       
$$$$/  $$$$ |$$ |  $$ |/$$$$$$$ |  $$ |/  |$$$$$$  |/$$$$$$$ |$$ |__$$ |$$ |__$$ |       
$$$/    $$$ |$$ |  $$ |$$    $$ |  $$  $$//     $$/ $$    $$ |$$    $$/ $$    $$/        
$$/      $$/ $$/   $$/  $$$$$$$/    $$$$/ $$$$$$$/   $$$$$$$/ $$$$$$$/  $$$$$$$/         
                                                              $$ |      $$ |             
                                                              $$ |      $$ |             
                                                              $$/       $$/              
 ________              __                                     __                         
/        |            /  |                                   /  |                        
$$$$$$$$/  __    __  _$$ |_     ______   ______    _______  _$$ |_     ______    ______  
$$ |__    /  \  /  |/ $$   |   /      \ /      \  /       |/ $$   |   /      \  /      \ 
$$    |   $$  \/$$/ $$$$$$/   /$$$$$$  |$$$$$$  |/$$$$$$$/ $$$$$$/   /$$$$$$  |/$$$$$$  |
$$$$$/     $$  $$<    $$ | __ $$ |  $$/ /    $$ |$$ |        $$ | __ $$ |  $$ |$$ |  $$/ 
$$ |_____  /$$$$  \   $$ |/  |$$ |     /$$$$$$$ |$$ \_____   $$ |/  |$$ \__$$ |$$ |      
$$       |/$$/ $$  |  $$  $$/ $$ |     $$    $$ |$$       |  $$  $$/ $$    $$/ $$ |      
$$$$$$$$/ $$/   $$/    $$$$/  $$/       $$$$$$$/  $$$$$$$/    $$$$/   $$$$$$/  $$/       
                                                                                         
 codet by f00k

 [1]  Get Wallpaper     [4] Get Profile Photos       [7] Get Voicenotes             

 [2]  Get Audios        [5] Get Stickers             [8] Uninstall Whatsapp           

 [3]  Get Images        [6] Get Videos               [9] exit
    ''','green','on_grey',['bold']))

    opt = input(c('Select your Option:', 'red', 'on_grey', ['bold']))    

    if opt == "1":
        print()
        print(c("Getting Wallpaper","red",'on_grey',['bold']))
        command("adb pull /sdcard/WhatsApp/Media/Wallpaper")
        menue()
    
    elif opt == "2":
        print()
        print(c("Getting Audio-Files","red","on_grey",['bold']))
        command("adb pull /sdcard/Whatsapp/Media/WhatsApp\ Audio")
        menue()
    
    elif opt == "3":
        print()
        print(c("Getting Images","red","on_grey",['bold']))
        command("adb pull /sdcard/Whatsapp/Media/WhatsApp\ Images")
        menue()

    elif opt == "4":
        print()
        print(c("Getting Profile Photos","red","on_grey",['bold']))
        command("adb pull /sdcard/Whatsapp/Media/Whatsapp\ Profile\ Photos")
        menue()

    elif opt == "5":
        print()
        print(c("Getting Stickers","red","on_grey",['bold']))
        command("adb pull /sdcard/Whatsapp/Media/WhatsApp\ Stickers")
        menue()
    
    elif opt == "6":
        print()
        print(c("Getting Stickers","red","on_grey",['bold']))
        command("adb pull /sdcard/Whatsapp/Media/WhatsApp\ Video")
        menue()

    elif opt == "7":
        print()
        print(c("Getting Voicenotes","red","on_grey",['bold']))
        command("adb pull /sdcard/WhatsApp/Media/'WhatsApp Voice Notes'")
        menue()

    elif opt == "8":
        print()
        print(c("Uninstalling WhatsApp from your Device","red","on_grey",['bold']))
        command("adb shell pm uninstall com.whatsapp")

    elif opt == "9":
        command("clear")
        print(c("Thank you for using F00ks WhatsappExtractor","red","on_grey",['bold']))

menue()


