from sys import stdout
import tkinter as tk
from tkinter import filedialog, ttk
import threading
import os
import subprocess
import time
from tkinter.constants import HORIZONTAL
from typing import Text
os.chdir('C:\\Users\\Admin\\Music\\Music')

"""
---------------------------------------------------

            Version : 2.94(beta)

---------------------------------------------------
"""

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Download"
        self.hi_there["command"] = self.Download
        self.hi_there.grid(row=0,column=2)

        self.L1 = tk.Label(self, text="Song Name or Link")
        self.L1.grid(row= 0, column=0)
        self.E1 = tk.Entry(self, bd =5)
        self.E1.grid(row=0, column=1)

        self.PRO1 = ttk.Progressbar(self, orient=HORIZONTAL,length=300, mode= 'indeterminate')
        self.PRO1.grid(row=3,column=1)

        self.L3 = tk.Label(self, text="Directory" )
        self.L3.grid(row= 1, column=0)
        self.L4 = tk.Label(self, text='C:\\')
        self.L4.grid(row=1, column=1)
        self.B2 = tk.Button(self, text='Browse', command=self.open_folder)
        self.B2.grid(row=1,column=2)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        #self.quit.pack(side="bottom")

    def msga(self,data):
        self.L2=tk.Label(self,text=data)
        self.L2.grid(row=2,column=1)
        self.L2.update_idletasks()

    def open_folder(self):
        self.folderDir = filedialog.askdirectory()
        if self.folderDir is None:
            self.folderDir='C:\\'
        self.L4.config(text=self.folderDir)
        
    def cmdDown(self,song):
        os.system(f'start cmd /c spotdl {song}')

    def processEffect(self):
        
        pr = 'Processing'
        self.PRO1.update_idletasks()
        self.msga(pr)
        time.sleep(1)
        self.L2.update_idletasks()
        root.update_idletasks()
        self.L2.grid_remove()
        if pr == 'Processing...':
            pr = 'Processing'
        pr = pr + '.'

    def Download(self):
        self.songName = self.E1.get()
        self.changeDir = self.folderDir
        self.PRO1['value']=0
        try:
            self.L2.grid_remove()
        except:
            pass
        if self.changeDir == '':
            pass
        else:
            self.changeDir=self.changeDir.replace("\\","\\\\")
            print(self.changeDir)
            os.chdir(self.changeDir)

        self.PRO1.start(10)
        self.msga('Processing')
        time.sleep(1)

        #self.processEffect()
        self.PRO1.config(mode='determinate')
        #os.system(f"cmd /c spotdl {self.songName}")
        #subprocess.run(['spotdl'], capture_output=True, text=True, input =self.songName.encode('utf-8')).stderr()
        self.msga('Started To Download')
        time.sleep(2)
        self.L2.grid_remove()
        self.PRO1.stop()
        self.cmdDown(self.songName)
        time.sleep(5)
        self.PRO1['value']=100
        self.msga('Completed')
        
        
        
        #out, err= p.communicate()
        #self.msga(out.decode('utf-8'))
        

    
root = tk.Tk()
app = Application(master=root)
app.mainloop()