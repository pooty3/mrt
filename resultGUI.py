from tkinter import *
import functions
def results(path):
    master=Tk()
    master.title('Reults')
    textbox=Label(master,text=str(path.time)+' minutes\n Path taken: '+functions.getpath(path))

    textbox.pack(side=TOP)
    master.lift()

    master.mainloop()
