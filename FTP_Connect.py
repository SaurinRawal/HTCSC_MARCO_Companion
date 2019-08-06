from ftplib import FTP
import getpass

HWI_FTP = 'ftp.hwi.buffalo.edu'
DOWNLOAD_LOG = 'HWI_FTP_LOG.txt'
OPTIONS = ['Display CWD',
           'Download File(s)',
           'Download All Files',
           'Show Download Log']


def connect_and_login():
    '''
    Connects and logs onto the HWI FTP server. Returns an FTP object.
    '''
    username = input('Enter your HWI FTP username: ')
    password = getpass.getpass('Enter your HWI FTP password: ')
    ftp = FTP(HWI_FTP)
    ftp.login(user=username, passwd=password)
    print(ftp.getwelcome())
    parent = ftp.pwd()
    return (ftp, parent)

def download_files(ftp, *args):
    for file in args:
        with open(file, 'wb') as write_file:
            ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

def download_files(ftp, files):
    for file in files:
        with open(file, 'wb') as write_file:
            ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

def download_all_files(ftp, parent):
    if ftp.pwd() is not parent:
        print('Starting directoy must be the parent')
        return None
    temp = []
    ftp.dir(dirs.append)
    dirs = parse_list(temp)

    for dir in dirs:
        ftp.cwd(dir)
        files = []
        ftp.dir(files.append)
        files = parse_list(files)
        download_files(ftp, files)


def parse_list(list):
    items = []
    for item in list:
        items.append(item.split(' ')[-1])
    return items

def display_options():
    for i, item in enumerate(OPTIONS):
        print('{}: {}'.format(i, item))

    selection = (input('Enter selection: '))
    selection = int(selection)
    print(type(selection))
    if selection_validation(selection) is True:
        return selection
    else:
        print('\nEnter a valid input')


def control_panel(selection, ftp, parent):
    if selection is 0:
        print(ftp.pwd())
    elif selection is 1:
        download_files(ftp, input('Enter comma seperated filenames: '))
    elif selection is 2:
        download_all_files(ftp, parent)
    elif selection is 3:
        print('Working on that')

def selection_validation(selection):

    if selection > len(OPTIONS) or selection < 0:
        print('not in range!')
        return False
    else:
        return True



def create_download_log():
    '''
    If it does not exist in the current directoy creates a download log file.
    '''
    if os.path.exists(DOWNLOAD_LOG):
        return True
    else:
        with open(DOWNLOAD_LOG, 'r') as log:
            log.write('HWI FTP DOWNLOAD LOG')
            log.write('-'*20)

def write_log_entry(entry):
    try:
        with open(DOWNLOAD_LOG, 'a+') as log:
            log.write(entry)
    except FileNotFoundError:
        create_download_log()


def read_download_log(download_log_path=DOWNLOAD_LOG):
    '''
    reads info in the download log as a dictionary with the file name as the key
    '''
