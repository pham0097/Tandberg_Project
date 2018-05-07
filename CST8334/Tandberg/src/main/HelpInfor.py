##########################################################
# CST8334 2018W-Software Development Project             #
# Author: Pham Thi Minh Phuong                           #
# April 7 2018                                           #
#update code from https://pypi.python.org/pypi/telnetlib3#
##########################################################

import tkinter  # import the tkinter
from tkinter import Tk, Frame, TOP, NO, NONE, Text,INSERT,Button, LEFT #import the components from the tkinter 


class FunctionIntroduction:  #create the class FunctionIntroduction to display the help information
    def __init__(self):  # define the constructor
        self
    
    def displayDescription(self): # create the method displayDescription
        root = Tk()    # assigne the root tkinter object.
        root.wm_title('Help ')   #Set the title 'help' for the GUI
        
        root.geometry("680x550")  #Set the size for the GUI
        text = Text(root)    #create the text varaible.
        
        s="""
        This is CST8334 HELP GUI 
        Tandberg system consist the VCS (video communication system)
        terminals supporting different network protocols. 
        The system can make voice and video call through the IP infrastructure. 
        The system is used for presentation with its TV size screen.
        System features which our team achieved: 
        •    Connecting all nodes to IP network and assigning IP address to them.  
        •    Establishing video and voice call between Tandberg’s terminals.
        •    Using Python control panel GUI in the System.
        •    Using MySQL Database to store users.
        •    Using Python to call Tandberg Library (API library) to make video, voice call, 
             split screen, share the PC screen to Tandberg.

        
        Author: Team Rocket
        Date: 2018-04-07
        """   # put the help information in string
        
        text.insert(INSERT,s)  # insert the Text
        text.pack()  # pack the text
        Button(root, text='Close',command=root.destroy).pack() # create close button for quit the GUI
        root.mainloop()  # start the GUI