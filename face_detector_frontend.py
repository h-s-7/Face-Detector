from tkinter import *
from tkinter import messagebox
import sys
from face_detector import *
root = Tk()
root.title('face detector')
root.geometry('150x150')
root.resizable(True,True)
root.iconbitmap('favicon.ico')
def add_user_button():
    
    add_user = Toplevel()
    add_user.title('Add User')
    add_user.resizable(True,True)
    add_user.geometry('400x100')

    def add_user_start_button():
    	new_user(add_user_id_entry.get(),1)
    	get_ready = Label(add_user,text = 'please smile you are infront of a camera')
    	get_ready.grid(row = 2,column = 0)
		

    add_user_id_label = Label(add_user,text = 'Enter your user_id : ')
    add_user_id_entry = Entry(add_user,width = 35,borderwidth = 2)
    add_user_start = Button(add_user,text = 'Start Camera',command = add_user_start_button)
	
    add_user_id_label.grid(row = 0,column = 0,pady = 10)
    add_user_id_entry.grid(row = 0,column = 1,pady = 10)
    add_user_start.grid(row = 1,column = 0,columnspan = 2)

def run_detector_button():
    
    #code for running face detector
    run_detector = Toplevel()
    run_detector.title('Detector')
    run_detector.resizable(True,True)
    run_detector.geometry('400x100')

    def detector_start_button():
    	status = detector(detector_user_id_entry.get(),1)
    	status_label = Label(run_detector,text = status)
    	status_label.grid(row = 2,column = 0)
    detector_user_id_label = Label(run_detector,text = 'Enter your user_id : ')
    detector_user_id_entry = Entry(run_detector,width = 35,borderwidth = 2)
    detector_start = Button(run_detector,text = 'Start Camera',command = detector_start_button)
	
    detector_user_id_label.grid(row = 0,column = 0,pady = 10)
    detector_user_id_entry.grid(row = 0,column = 1,pady = 10)
    detector_start.grid(row = 1,column = 0,columnspan = 2)	
	
#function not working properly
def exit_option():
    response = messagebox.askyesno("Popup","Do you want to exit?")
    if response == 1:
        root.quit


r = IntVar()

rb1 = Radiobutton(root,text = 'Add User',variable = r,value = 1,command = add_user_button,anchor = W,justify = LEFT)
rb2 = Radiobutton(root,text = 'Run face detector',variable = r,value = 2,command = run_detector_button,anchor = W,justify = LEFT)
rb3 = Radiobutton(root,text = 'exit',variable = r,value = 3,command = exit_option,anchor = W,justify = LEFT)

rb1.grid(row = 0,column = 0,sticky = W)
rb2.grid(row = 1,column = 0,sticky = W)
rb3.grid(row = 2,column = 0,sticky = W)

root.mainloop()
