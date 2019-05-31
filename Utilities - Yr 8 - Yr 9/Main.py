####################################################################################
#                                 Code made by L0R3N3O                             #
#                          Visit me on Discord: L0R3N3O#4742                       #
#                           Year 8-9 side-project, 2018-2019                       #
#                   Feel free to edit to include personal commands,                #
#                           please see comments inside code                        #
####################################################################################

import time #Current Date/Time
import os #To open files with
import datetime #Current Date/Time

def close_screen(): 
    exit()

def main_manage():
      global screen
      screen = Tk()
      screen.geometry("1080x640")
      screen.title("User Management v0.5")
      Label(text = "Menu - Admin Console ", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
      Label(text = "").pack()
      Button(text = "Close",height = "1", width = "10", command = close_screen).pack()
      Label(text = "").pack()
      Button(text = "Open", height = "2", width = "30", command = open_util).pack()
      Label(text = "").pack()
      Button(text = "Current Time",height = "2", width = "30", command = register).pack()
      Label(text = "").pack()
      Button(text = "Help?",height = "2", width = "30", command =  main_info).pack()
      print("User Management v0.5 Tool started by: pyTkinterService")

def time_util():
      lobal screen
      screen = Tk()
      screen.geometry("1080x640")
      screen.title("Utilities Tool - v2.0.0")
      Label(text = "Current time/date", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
      Label(text = "").pack()
      Label(text = datetime.datetime.now().time()).pack()
      print("Current Time/Date is:", datetime.datetime.now().time())


def open_util():
        global screen
        screen = Tk()
        screen.geometry("1080x640")
        screen.title("User Management v0.5")
        Label(text = "Menu - Admin Console ", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
        Label(text = "").pack()
        Button(text = "Close",height = "1", width = "10", command = close_screen).pack()
        Label(text = "").pack()
        Button(text = "Start Steam", height = "2", width = "30", command = login).pack() #Copy and paste Line 52-53 below
        Label(text = "").pack()
        Button(text = "Start Discord",height = "2", width = "30", command = register).pack()
        Label(text = "").pack()
        Button(text = "Help?",height = "2", width = "30", command =  main_info).pack()
        print("User Management v0.5 Tool started by: pyTkinterService")

def steam_os(): # Copy and paste this below then replace os.startfile('C:\Program Files (x86)\Steam') with os.startfile('Wherever your program installed is saved')
      os.startfile('C:\Program Files (x86)\Steam')

def discord_os():
      os.startfile