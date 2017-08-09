#!/usr/bin/python

import Tkinter as tk

class Application(tk.Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.quitBtn = tk.Button(self, text='Quit', fg='red', command=self.quit)
        #self.quitBtn["command"] = self.quit # is an alternative
        self.quitBtn.pack({"side": "left"})

        self.hi_there = tk.Button(self, text='Hello', command=self.say_hi)
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
