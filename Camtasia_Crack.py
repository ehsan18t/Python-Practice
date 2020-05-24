# CAMTASIA CRACK SCRIPT V1.01
# AUTHOR: Ahsan40 / Ahsan400
# CREATED ON: 2017
# INITIAL RELEASE: 12 May 2020
# LAST UPDATED: 24 May 2020
# TARGETED PYTHON: 3.7, 3.8, 3.9 and newer
# TARGETED OS: All Windows with python installed
# WORKS ON: Camtasia 2019.0.10 and all previous version
# TESTED ON: Camtasia 8, 9, 2018, 2019
# NOTE: It doesn't works with 2020 and newer version
# Special thanks to @RealShourov
# Don't use it for evil purpose
# Created only for learning purpose


# Importing necessary modules
import ctypes
import os
import re
import sys
import time

import win32api
import win32con

# Title
os.system("TITLE Camtasia Patcher v1.01")

# Window Size
os.system("mode con:cols=55 lines=17")

# Window Color
os.system("COLOR 0A")

# Cursor Classes
# REF: https://stackoverflow.com/questions/5174810/how-to-turn-off-blinking-cursor-in-command-window
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
# REF: https://www.geeksforgeeks.org/print-colors-python-terminal/
# MC Stands for 'My Colors
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
    RED_W = '\033[1;37;41m'  # RED_W stand for RED BG + White Text
    GRE_W = '\033[1;37;42m'  # First 3 character of color name then
    YEL_W = '\033[1;37;43m'  # First character of text color
    BLU_W = '\033[1;37;44m'  # Same method applied for rest of the color
    PUR_W = '\033[1;37;45m'
    CYA_B = '\033[0;30;46m'


# Patched Define variable
already_patched = 'NO'

# Info
print(MC.RED + '*******************************************************\n'
               '*                                                     *\n'
               '*                Created By Ahsan400                  *\n'
               '*   Supported to 2019.0.10 and all previous version   *\n'
               '*                                                     *\n'
               '*******************************************************\n' + MC.END)

# Checking Data Directory
initial_path = ''  # Declaring variable to store Data directory of Camtasia
check_path = ''  # Declaring temp path variable to check if it exist
print('=> Finding Installed Directory...')
time.sleep(1)  # Adding 1s Delay
for i in range(ord('A'), ord('Z') + 1):  # Loop for generate 'A' to 'Z' character
    check_path = chr(i) + r':\ProgramData\TechSmith'  # Adding generated character to complete the path
    if os.path.exists(check_path):  # Checking if path exist
        initial_path = check_path  # Storing generated path to 'initial_path' (if it exist)
        break  # Exiting from loop

# Checking if data dir is exist (If it exist, it's length will be 24, no exception possible)
if len(initial_path) != 24:
    print('\n\n\n\n' +
          MC.RED_W + '                                                       ' + MC.END)
    print(MC.RED_W + '               Camtasia Not Installed!                 ' + MC.END)
    print(MC.RED_W + '                                                       ' + MC.END)
    input(MC.PUR_W + '                 Press enter to exit                   ' + MC.END)
    sys.exit(0)

# Specifying Camtasia REG DATA PATH
full_list = []  # Declaring Array to list all the Dir inside 'initial_path' root
print('=> Finding Program Data PATH...')
time.sleep(1)  # Adding 1s Delay
for d in os.listdir(initial_path):  # Loop to find all available directory inside 'initial_path' folder
    if os.path.isdir(os.path.join(initial_path, d)):  # Condition to add path to list if it's a 'dir' and in root dir
        full_list.append(d)  # Adding All Search Results to 'full_list' Array

# Checking if Multiple Version of Camtasia Installed
r = re.compile("Camtasia Studio.*")  # Searching in 'full_list' for "Camtasia Studio.*" regex
path_name_list = list(filter(r.match, full_list))  # Creating List with Filtered Path Names
path_list_len = len(path_name_list)  # Measuring 'path_name_list' size

# Removing Empty folders from 'path_name_list' if list contains more than 1 value
list_line_number: int = 0  # Will use it to print line number of current text from final 'path_name_list'
list_index = list_line_number  # Declaring 'list_index = list_count' and it's value is 0 (zero) right now
if path_list_len > 1:  # Checking if list has at least one value
    for p in range(0, path_list_len):
        path_name_temp = (path_name_list[list_index])  # Storing path name temporarily
        check_path = initial_path + r'\ '.strip() + path_name_temp + r'\RegInfo.ini'
        if os.path.isfile(check_path):  # If 'check_path' exist increasing 'list_index' to check next one
            list_index += 1
        else:  # If 'check_path' is not exist then removing that and reducing 'list_index' to check same index again
            path_name_list.remove(path_name_temp)  # Removing the non-exist from 'path_name_list'
            list_index -= 1  # and reducing 'list_index' by 1 to check this index again

# Start working with filtered list of 'path_name_list' from here
program_selector_input: int = 0  # using for selecting program index if more than one installed (default = 0)
path_list_len = len(path_name_list)  # Again Measuring new 'path_name_list' size
if path_list_len >= 1:  # Checking if list has at least one value
    if path_list_len > 1:  # Checking if list is greater then 1
        installed_camtasia_count = str(path_list_len)  # will store how many camtasia installed
        print(MC.RED_W + '=> ' + installed_camtasia_count + ' Version of Camtasia installed!' + MC.END)
        for p in range(path_list_len):  # This loop with repeat (path_list_len) times
            list_line_number += 1  # Starting count from 1 and will increase with every repeat
            path_name_temp = (path_name_list[p])  # Storing path name temporarily ('p' is counter of this loop)
            print('        ' + str(list_line_number) + '. ' + path_name_temp)  # Printing installed Programs
        while True:
            try:
                show_cursor()  # Enabling cursor to take user input
                program_selector_input = int(input('\n' + MC.CYA_B + '=> Please Select one to CRACK:' + MC.END + ' '))
                hide_cursor()  # Disabling cursor again
                if 0 < program_selector_input <= list_line_number:  # Making sure that '0 < input <= list_line_number'
                    program_selector_input -= 1  # Reducing 1 to adjust user input with list index
                    break  # Exiting from loop
                else:  # Will be printed if user input a number less then equ 0 or greater then equ 'list_line_number'
                    print(MC.RED_W + "     INVALID OPTION SELECTED! PLEASE TRY AGAIN!" + MC.END)
            except Exception as e:  # Will be printed if user input anything other than integer
                e.msg = MC.RED_W + '     INVALID OPTION SELECTED! PLEASE TRY AGAIN!' + MC.END
                print(e.msg)

else:  # if path_name_list is empty this will be printed
    print('\n\n\n' +
          MC.RED_W + '                                                       ' + MC.END)
    print(MC.RED_W + '               Camtasia Not Installed!                 ' + MC.END)
    print(MC.RED_W + '                                                       ' + MC.END)
    input(MC.PUR_W + '                 Press enter to exit                   ' + MC.END)
    sys.exit(0)

path_name = path_name_list[program_selector_input]  # Final/Selected path name
path_address = initial_path + r'\ '.strip() + path_name  # Final path address

# Checking If Already Patched or not
reg_data = ''  # Declaring empty variable
print('=> Checking Program Status...')
time.sleep(1)  # Adding 1s Delay
reg_file_name = 'RegInfo.ini'  # Declaring variable to store file name
reg_file_address = path_address + r'\ '.strip() + reg_file_name  # Generating File Address
if os.path.isfile(reg_file_address):  # Checking if file exist
    combination = re.compile('RegisteredTo=.*?')  # Declaring RegEx format
    for line in open(reg_file_address):  # Loop for finding specific line in reg_file ('line' is loop repeat counter)
        temp_line = combination.match(line)  # Storing match data in 'temp_line'
        if temp_line:  # If 'temp_line == RegEx Combination' (if match the text we are searching)
            reg_data = line  # Adding Matched line in 'reg_data' variable
    if reg_data == 'RegisteredTo=Ahsan\n':  # Checking if already patched or not
        already_patched = 'YES'  # If condition true this variable will set as YES (Default: NO)
        print('\n\n')
        print(MC.BLU_W + '                                                       ' + MC.END)
        print(MC.BLU_W + '              Camtasia Already Patched                 ' + MC.END)
        print(MC.BLU_W + '                                                       ' + MC.END)
        input(MC.PUR_W + '                 Press enter to exit                   ' + MC.END)
        sys.exit(0)

# Removing 'RegInfo.ini' file if already exist
print('=> Patching ' + path_name + '...')
time.sleep(1)  # Adding 1s Delay
if os.path.isfile(reg_file_address):  # Checking if 'RegInfo.ini' file is already exist at 'reg_file_address'
    win32api.SetFileAttributes(reg_file_address, win32con.FILE_ATTRIBUTE_NORMAL)  # Changing file attribute to normal
    os.remove(reg_file_address)  # Removing file

# Creating REG file for Camtasia to the data folder(reg_file_address)
file = open(reg_file_address, 'w')  # Opening a file named 'RegInfo.ini' at 'reg_file_address' to write
file.write(
    '[RegistrationInfo]\n'
    'ValidationData3=0\n'
    'RegistrationKey=CVY69-FCCZA-CJWAV-YFDHB-CBEBB\n'
    'RegisteredTo=Ahsan\n'
    'ValidationData1=\n'
    'ValidationData2=1\n')
file.close()  # Closing the opened file

# Changing 'RegInfo.ini' file Attribute to READ ONLY
win32api.SetFileAttributes(reg_file_address, win32con.FILE_ATTRIBUTE_READONLY)  # [Most Important]

print('\n\n')
print(MC.GRE_W + '                                                       ' + MC.END)
print(MC.GRE_W + '                 Operation Successful                  ' + MC.END)
print(MC.GRE_W + '                                                       ' + MC.END)
input(MC.PUR_W + '                 Press enter to exit                   ' + MC.END)
sys.exit(0)
