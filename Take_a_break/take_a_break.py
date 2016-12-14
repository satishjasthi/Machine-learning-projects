import webbrowser #library to open webfiles
import time       #library to track time

from pygame import mixer # library to play song

from Tkinter import * #  library for creating pop up messages
import tkMessageBox   

name = raw_input('Please enter your name \n')

work_time = raw_input('\n Hi ' + name + ' Please enter the number of minutes you would like to work :) \n')
work_time = float(work_time) #converting work_time from string format to int
work_time = work_time * 60

break_time = raw_input('\n Hi ' + name + ' Please enter your break time in minutes :) \n')
break_time = float(break_time)
break_time = break_time * 60

SongOrVideoLocationInternet = ""
SongOrVideoLocationSystem = ""
var0 = raw_input('Is your break time song located in system?(y/n)')



count  = 0

if var0 == 'y':
         SongOrVideoLocationSystem = raw_input('\n' + name + ' Please enter your song location in system \n')
         SongOrVideoLocation = SongOrVideoLocationSystem

else:
         
         SongOrVideoLocationInternet = raw_input('\n' + name + ' Please enter song''s url \n')
         SongOrVideoLocation = SongOrVideoLocationInternet




while count <4:
        print('\n Current working session: ' + time.ctime())#prints current date and time
	time.sleep(work_time) # pauses the program for given number of seconds ,here it's 10 sec
	root = Tk().withdraw()  # hiding the main window
	var1 = tkMessageBox.askyesno("Break Time", ('Hi ' + name + " would you like to take a break? "))

	if (var1 == True) & (SongOrVideoLocation == SongOrVideoLocationInternet):
		 webbrowser.open(SongOrVideoLocation)
		 count += 1
                 time.sleep(break_time)
                 var3  = tkMessageBox.askyesno("Back to work","Hi " + name + " your break session is over,would you like to go back to work?")
                 if var3 == True:
                          continue
                 else :
                          break
        elif (var1 == True) & (SongOrVideoLocation == SongOrVideoLocationSystem):
                   try: #code to play song
                       mixer.init()
                       mixer.music.load(SongOrVideoLocation)
                       mixer.music.play()
  
                   except:
                          print("the file should be in mp3 format")

                   count += 1
                   time.sleep(break_time)
                   var3  = tkMessageBox.askyesno("Back to work","Hi " + name + " your break session is over,would you like to go back to work?")
                   if var3 == True:
                            continue
                   else :
                            break


	else:
                var2 = tkMessageBox.askyesno("Back to work",("Hi " + name + " would you like to continue your work?"))
                if var2 == True:
                         continue
		else:
                         break








