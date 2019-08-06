from FTP_Connect import *
import sys
import os

def main():
    print('Welcome to MARCO FTP companion.')
    ftp, parent = connect_and_login()  # connect to HWI FTP

    while True:
        
        print('Run a command by typing corresponding number')
        selection = display_options()
        if selection is not None:
            control_panel(selection, ftp, parent)
        sys.stdout.write('\r')



if __name__ == '__main__':
    main()
