#!/usr/bin/python

import Tkinter as tk

class Application(tk.Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = tk.Button(self, text='Quit', fg='red')

        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello"
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})
        self.configure(background='blue')

    def __init__(self, master=None):
        master.minsize(width=666, height=666)
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = tk.Tk()
root.configure(background='grey')
app = Application(master=root)
app.mainloop()
root.destroy()
