from tkinter import *
import resultGUI
import functions
import program



class GUI():
    def __init__(self):
        self.master=Tk()
        self.start=StringVar()
        self.end=StringVar()

        self.master.title('Shortest MRT Time Finder')

        self.master.geometry('1500x800')
        map = PhotoImage(file="mrt.png")
        self.maplabel = Label(self.master, image=map)
        self.maplabel.pack(side=LEFT)
        instruction = Label(self.master, text="Put the Starting Point\n and Ending Point.\n e.g.(EW1)")
        instruction.pack(side=TOP)
        Label(self.master, text="Starting point:").pack(side=TOP)
        self.startentry = Entry(self.master,textvariable=self.start)
        self.startentry.pack(side=TOP)
        Label(self.master, text="Ending point:").pack(side=TOP)
        self.endentry = Entry(self.master,textvariable=self.end)
        self.endentry.pack(side=TOP)
        gobutton = Button(text="Find shortest time!", command=self.gofunction)
        gobutton.pack(side=TOP)
        self.validlabel=Label(self.master)
        self.validlabel.pack(side=TOP)
        self.timelabel=Label(self.master)
        self.timelabel.pack(side=TOP)
        self.master.mainloop()

    def gofunction(self):

        starting=self.start.get()
        ending=self.end.get()
        if(starting!=ending and functions.validstation(starting) and functions.validstation(ending)):
            self.validlabel.config(text='Valid stations. Wait awhile sir.\n Take around 1-5minutes\n depending on how long\n it is and how good \nyour computer is.')
            path=program.go(starting,ending)
            self.timelabel.config(text='Time taken is '+str(path.time)+'.')
            resultGUI.results(path)


        else:
           self.validlabel.config(text='Not valid stations')
           self.timelabel.config(text='')






GUI()