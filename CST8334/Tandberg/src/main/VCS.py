
##########################################################
# CST8334 2018W-Software Development Project             #
# Author: Bo Liu and Binh Minh Do                        #
# April 7 2018                                           #
# Software GUI                                           #
#                                                        #
##########################################################

import os
from tkinter import *
import HelpInfor #import the class FunctionIntroduction
import webbrowser

class DisplayDataSetGUI:  #Define class  DisplayDataSetGUI

    def __init__(self, master):  #define the constructor 
        self.master = master     # assigne the master with value
        #master.title("A simple GUI")
        master.wm_title('Tandberg VCS -- CST8334 Rocket Team 2')
        fm=Frame(master, width=750,height=550) # initiate the frame 
        fm.pack(side=TOP, expand=NO, fill=NONE)
        master.geometry("800x600")  # set the master gui dimension 


        Label(fm, text='Genereal:').grid(row=0, column=0) # create label
        Button(fm, text='Tandberg', width=10, command=lambda: self.openWeb('http://10.50.18.143/')).grid(row=0, column=1)  # create buttons
        Button(fm, text='Rocket', width=10,command=lambda: self.openWeb('http://www.algonquinstudents.ca/~do000045/Rocket%20v1/index.html')).grid(row=0, column=2)
        b = HelpInfor.FunctionIntroduction()  # instantiate the FunctionIntroduction
        self.help_button = Button(fm, text="Help", width=10,command=b.displayDescription)  # configure help button on the gui
        self.help_button.grid(row=0, column=3)  # put the button on grid 0,1 position


        Label(fm, text='Call Control:').grid(row=1, column=0)
        Button(fm, text='Call',width=10,command=lambda:  os.system('call.py')).grid(row=1, column=1)
        Button(fm, text='Answer', width=10, command=lambda: os.system('answer.py')).grid(row=1, column=2)
        Button(fm, text='Disconect', width=10, command=lambda: os.system('disconect.py')).grid(row=1, column=3)


        Label(fm, text='Camera Control:').grid(row=2, column=0)
        Button(fm, text='Turn right',width=10,command=lambda:  os.system('camright.py')).grid(row=2, column=1)
        Button(fm, text='Turn left',width=10,command=lambda:   os.system('camleft.py')).grid(row=2, column=2)
        Button(fm, text='Turn up', width=10, command=lambda: os.system('camup.py')).grid(row=2, column=3)
        Button(fm, text='Turn down', width=10, command=lambda: os.system('camdown.py')).grid(row=2, column=4)

        Label(fm, text='Mic Control').grid(row=3, column=0)
        Button(fm, text='Turn on',width=10,command=lambda:  os.system('micon.py')).grid(row=3, column=1)
        Button(fm, text='Turn off',width=10,command=lambda:  os.system('micoff.py')).grid(row=3, column=2)


        Label(fm, text='Screen Setting').grid(row=4, column=0)
        Button(fm, text='Slip', width=10, command=lambda: os.system('screenslip.py')).grid(row=4,column=1)
        Button(fm, text='Full', width=10, command=lambda: os.system('screenfull.py')).grid(row=4,column=2)


        Label(fm, text='VNC').grid(row=5, column=0)
        Button(fm, text='Setup',width=10,command=lambda:  os.system('vncsetup.py')).grid(row=5, column=1)
        Button(fm, text='Connect', width=10, command=lambda: os.system('vncconnect.py')).grid(row=5, column=2)
        Button(fm, text='Start',width=10,command=lambda:  os.system('vncstart.py')).grid(row=5, column=3)
        Button(fm, text='Stop',width=10,command=lambda:  os.system('vncstop.py')).grid(row=5, column=4)



    def openWeb(self, event):
        """ handle button click event and output text from entry area"""
        webbrowser.open(event)
        
   
root = Tk() # instantiate root
root.wm_iconbitmap('r.ico') # set icon
my_gui = DisplayDataSetGUI(root) #instantiate my_gui
root.mainloop()  # start gui display