import os

defaultDrive ='C'
"""
-----------------------------------------

            Version : 1.35 (beta)

-----------------------------------------
"""

try:
    folderLoc = open(f'{defaultDrive}:\\data.txt','r+')
    folder = folderLoc.readlines()
    folder = folder[1]
    folderLoc.close()
except FileNotFoundError:
    folderLoc = open(f'{defaultDrive}:\\data.txt','w+')
    folderLoc.write(f"{defaultDrive}")
    folderLoc.write(f"{defaultDrive}:\\")
    folder = f"{defaultDrive}:\\"
    folderLoc.close()
except PermissionError:
    print("Permission error in C drive")
    defaultDrive = input("Enter the drive letter in capital like 'C' : ")
    folderLoc = open(f'{defaultDrive}:\\data.txt','w+')
    folderLoc.write(f"{defaultDrive}")
    folderLoc.write(f"{defaultDrive}:\\")
    folder = f"{defaultDrive}:\\"
    folderLoc.close()
except:
    folderLoc = open(f'{defaultDrive}:\\data.txt','w+')
    folderLoc.write(f"{defaultDrive}")
    folderLoc.write(f"{defaultDrive}:\\")
    folder = f"{defaultDrive}:\\"
    folderLoc.close()

class Download():
    def __init__(self,folder):
        self.folder = folder[2]
        self.dir = os.getcwd()

    def changeDir(self,fold):
        os.chdir(fold)

    def currentDir(self):
       return self.dir

    def spotifyMusic(self, option):
        os.system(f"cmd /c spotdl {option}")
    
def main():
    print()
    print('1. Paste link to download the song')
    print('2. Settings')
    print('3. Exit')
    print()

    option = input("Enter the option number : ")

    try:
        while True:
            if option == '2':
                while True:

                    print()
                    print('1. Current download location')
                    print('2. Change download location')
                    print('3. Change FFmpeg location')
                    print('4. Back')
                    print()
                    
                    option = input("Enter the option number : ")

                    if option == '2':
                        newLoc = input("Enter the new location like 'C:\\Users\\Name\\Desktop\\File' format : ")
                        folderLoc = open(f'{defaultDrive}:\\data.txt','w+')
                        folderLoc.write(defaultDrive)
                        folderLoc.write(newLoc)
                        folderLoc.close()
                        Download.changeDir
                    
                    elif option == '3':
                        print()
                        print('Please add location FFmpeg as path for faster downloading and locating the file!!!')
                        print()
                        
                    elif option == '4':
                        print()
                        print('Any change will applied after the program restart!!!')
                        print()
                        break
                    
                    elif option == '1':
                        print()
                        Download.currentDir()
                        print()

            elif option == '3':
                break

            elif option == '1':
                print()
                print('Just type the name of song or \nlink of song in spotify or \nplaylist link in sportify or \nlocation of the text file with contain the name of the song \nand press enter!!!')
                print()
            else:
                Download.spotifyMusic(option=option)
        
    except:
        print()
        print('Something happend. Try Again!!! \nCheck your internet and firewall \nCheck link is correct or avaiable')
        print()


if __name__ == "__main__":
    main()
    

