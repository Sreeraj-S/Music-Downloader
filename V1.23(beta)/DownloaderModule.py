import os

"""
-----------------------------------------

            Version : 1.23 (beta)

-----------------------------------------
"""

try:
    folderLoc = open('C:\\data.txt','r+')
    folder = folderLoc.readline()
    folderLoc.close()
except:
    folderLoc = open('C:\\data.txt','w+')
    folderLoc.write("C:\\")
    folder = "C:\\"
    folderLoc.close()

class Download():
    def __init__(self,folder):
        self.folder = folder
        self.dir = os.getcwd()
    def changeDir(self):
        os.chdir(self.folder)
    def currentDir(self):
       return self.dir
    def spotifyMusic(self, option):
        os.system(f"cmd /c spotdl {option}")

