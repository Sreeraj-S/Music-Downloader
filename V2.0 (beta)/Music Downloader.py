import tkinter as tk
import os
import subprocess

os.chdir('C:\\Users\\Admin\\Music\\Music')

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
        self.hi_there.grid(row=2,column=1)

        self.L1 = tk.Label(self, text="Song Name or Link")
        self.L1.grid(row= 0, column=0)
        self.E1 = tk.Entry(self, bd =5)
        self.E1.grid(row=0, column=2)

        self.L3 = tk.Label(self, text="Directory" )
        self.L3.grid(row= 1, column=0)
        self.E2 = tk.Entry(self, bd =5)
        self.E2.grid(row=1, column=2)


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        #self.quit.pack(side="bottom")
    
    def msga(self,data):
        self.L2=tk.Label(self,text=data)
        self.L2.grid(row=3,column=1)

    def Download(self):
        self.songName = self.E1.get()
        self.changeDir = self.E2.get()
        if self.changeDir == '':
            pass
        else:
            self.changeDir=self.changeDir.replace("\\","\\\\")
            os.chdir(self.changeDir)
        #os.system(f"cmd /c spotdl {self.songName}")
        #subprocess.run(['spotdl'], capture_output=True, text=True, input =self.songName.encode('utf-8')).stderr()
        try:
            self.L2.pack_forget()
        except:
            pass
        cmd = ['spotdl', self.songName]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
        out, err= p.communicate()
        self.msga(out.decode('utf-8'))
        

    
root = tk.Tk()
app = Application(master=root)
app.mainloop()