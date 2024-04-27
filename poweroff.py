import os

Shut_down = input("Would you like to shut down your PC? Y/N: ")
if Shut_down == "Y":
    os.system('shutdown -s')
else:
    print("Your PC won't be shut down!")