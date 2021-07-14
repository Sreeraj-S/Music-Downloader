import os

"""
-----------------------------------------

            Version : 1.0
            
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

os.chdir(folder)
while True:
    print()
    print('1. Paste link to download the song')
    print('2. Settings')
    print('3. Exit')
    print()

    option = input("Enter the option number : ")

    try:
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
                    folderLoc = open('C:\\data.txt','w+')
                    folderLoc.write(newLoc)
                    folderLoc.close()
                
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
                    print(os.getcwd())
                    print()

        elif option == '3':
            break

        elif option == '1':
            print()
            print('Just type the name of song or \nlink of song in spotify or \nplaylist link in sportify or \nlocation of the text file with contain the name of the song \nand press enter!!!')
            print()
        else:
            os.system(f"cmd /c spotdl {option}")
    
    except:
        print()
        print('Something happend. Try Again!!! \nCheck your internet and firewall \nCheck link is correct or avaiable')
        print()
