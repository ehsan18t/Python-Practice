# CAMTASIA CRACK SCRIPT V1.0
# AUTHOR: Ahsan40
# CREATED ON: 2017
# INITIAL RELEASE: 12 May 2020
# TARGETED PYTHON: 3.7, 3.8, 3.9
# TARGETED OS: All Windows with python installed
# WORKS ON: Camtasia 2019.0.10 and all previous version
# TESTED ON: Camtasia 8, 9, 2018, 2019
# NOTE: It doesn't works on 2020
# Special thanks to @RealShourov
# Don't use it for evil purpose
# Created only for learning purpose


# Importing necessary modules
import ctypes
import os
import re
import shutil
import sys
import win32api
import win32con
import time

# Title
os.system("TITLE Camtasia Patcher v1.0")

# Window Size
os.system("mode con:cols=55 lines=17")

# Window Color
os.system("COLOR 0A")

# Cursor Classes
if os.name == 'nt':
    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()


def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


# Hiding Cursor
hide_cursor()


# Color Classes
# Only Works in Windows
# Visit this link for More https://www.geeksforgeeks.org/print-colors-python-terminal/
class MC:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'
    BG_GRAY = '\033[40m'
    RED = '\033[91m'
    BG_RED = '\033[41m'
    GREEN = '\033[92m'
    BG_GREEN = '\033[42m'
    YELLOW = '\033[93m'
    BG_YELLOW = '\033[43m'
    BLUE = '\033[94m'
    BG_BLUE = '\033[44m'
    PURPLE = '\033[95m'
    BG_PURPLE = '\033[45m'
    CYAN = '\033[96m'
    BG_CYAN = '\033[46m'
    WHITE = '\033[97m'
    BG_WHITE = '\033[47m'
    BLACK = '\033[30m'
    BG_BLACK = '\033[0;30;37m'
    END = '\033[0;30;32m'
    REDW = '\033[1;37;41m'
    GREW = '\033[1;37;42m'
    YELW = '\033[1;37;43m'
    BLUW = '\033[1;37;44m'
    PURW = '\033[1;37;45m'
    CYAW = '\033[0;30;46m'


# Patched Define variable
already_patched = 'NO'

# Count Variable
list_count: int = 0
question: int = 0

# Info
print(MC.RED + '*******************************************************\n'
               '*                                                     *\n'
               '*                Created By Ahsan400                  *\n'
               '*   Supported to 2019.0.10 and all previous version   *\n'
               '*                                                     *\n'
               '*******************************************************\n' + MC.END)

# Checking Data Directory
print('=> Finding Installed Directory...')
time.sleep(1)   # Adding 1s Delay
initial_path = ''
test_path = ''
for i in range(ord('A'), ord('Z') + 1):
    test_path = chr(i) + r':\ProgramData\TechSmith'
    if os.path.exists(test_path):
        initial_path = test_path
        break
    else:
        pass
if len(initial_path) > 0:
    pass
else:
    print('\n\n\n\n' +
          MC.REDW + '                                                       ' + MC.END)
    print(MC.REDW + '               Camtasia Not Installed!                 ' + MC.END)
    print(MC.REDW + '                                                       ' + MC.END)
    input(MC.PURW + '                 Press enter to exit                   ' + MC.END)
    sys.exit(0)

# Specifying Camtasia REG DATA PATH
print('=> Finding Program Data PATH...')
time.sleep(1)   # Adding 1s Delay
plist = []      # Declaring Array to list all the Dir inside initial_path's root
for d in os.listdir(initial_path):
    if os.path.isdir(os.path.join(initial_path, d)):
        plist.append(d)     # Adding Search Results to plist Array

# Checking if Multiple Version of Camtasia Installed
r = re.compile("Camtasia Studio.*")
path_named = list(filter(r.match, plist))
plen = len(path_named)
list_count_2 = list_count
if plen > 1:
    for p in range(0, plen):
        path_name_c = (path_named[list_count_2])
        test_path = initial_path + r'\ '.strip() + path_name_c + r'\RegInfo.ini'
        if os.path.isfile(test_path):
            list_count_2 += 1
        else:
            path_named.remove(path_name_c)
            list_count_2 -= 1

if len(path_named) >= 1:
    plen = len(path_named)
    if plen > 1:
        n_count = str(plen)
        print(MC.REDW + '=> ' + n_count + ' Version of Camtasia installed!' + MC.END)
        for p in range(plen):
            list_count += 1
            l_count = str(list_count)
            path_named = (plist[p])
            print('        ' + l_count + '. ' + path_named)
        while True:
            try:
                show_cursor()
                question = int(input('\n' + MC.CYAW + '=> Please Select one to CRACK:' + MC.END + ' '))
                if 0 < question <= list_count:
                    question -= 1
                    break
                else:
                    print(MC.REDW + "     INVALID OPTION SELECTED! PLEASE TRY AGAIN!" + MC.END)
            except:
                print(MC.REDW + "     INVALID OPTION SELECTED! PLEASE TRY AGAIN!" + MC.END)

else:
    print('\n\n\n' +
          MC.REDW + '                                                       ' + MC.END)
    print(MC.REDW + '               Camtasia Not Installed!                 ' + MC.END)
    print(MC.REDW + '                                                       ' + MC.END)
    input(MC.PURW + '                 Press enter to exit                   ' + MC.END)
    sys.exit(0)

hide_cursor()
path_name = plist[question]
path = initial_path + r'\ '.strip() + path_name

# Checking If Already Patched or not
print('=> Checking Program Status...')
time.sleep(1)   # Adding 1s Delay
atr_file = 'RegInfo.ini'
file_t = path + r'\ '.strip() + atr_file
if os.path.isfile(file_t):
    pat = re.compile('RegisteredTo=.*?')
    for line in open(file_t):
        m = pat.match(line)
        if m:
            regdata = line
            if regdata == 'RegisteredTo=Ahsan\n':
                already_patched = 'YES'
                print('\n\n')
                print(MC.BLUW + '                                                       ' + MC.END)
                print(MC.BLUW + '              Camtasia Already Patched                 ' + MC.END)
                print(MC.BLUW + '                                                       ' + MC.END)
                input(MC.PURW + '                 Press enter to exit                   ' + MC.END)
                sys.exit(0)

# Remove file if already exist
print('=> Patching ' + path_name + '...')
time.sleep(1)   # Adding 1s Delay
atr_file = 'RegInfo.ini'
file_t = path + r'\ '.strip() + atr_file
if os.path.isfile(file_t):
    win32api.SetFileAttributes(file_t, win32con.FILE_ATTRIBUTE_NORMAL)
    os.remove(file_t)

# Creating REG file for Camtasia
file = open('RegInfo.ini', 'w')
file.write(
    '[RegistrationInfo]\n'
    'ValidationData3=0\n'
    'RegistrationKey=CVY69-FCCZA-CJWAV-YFDHB-CBEBB\n'
    'RegisteredTo=Ahsan\n'
    'ValidationData1=\n'
    'ValidationData2=1\n')
file.close()

# Moving Custom REG File
shutil.move('RegInfo.ini', path + r'\RegInfo.ini')

# Changing REG file Attribute to READ ONLY
atr_file = 'RegInfo.ini'
file = path + r'\ '.strip() + atr_file
win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_READONLY)

# Remove Created File If it's not moved for some reason
if os.path.isfile('RegInfo.ini'):
    os.remove('RegInfo.ini')

print('\n\n')
print(MC.GREW + '                                                       ' + MC.END)
print(MC.GREW + '                 Operation Successful                  ' + MC.END)
print(MC.GREW + '                                                       ' + MC.END)
input(MC.PURW + '                 Press enter to exit                   ' + MC.END)
sys.exit(0)
