## This is the File which will contain all of the messy code and functions
from __future__ import generators
import socket, platform, sys, wmi, os, getpass, ctypes, subprocess, win32file, datetime, win32com.client, win32net, win32netcon
import win32com.client 

# System Information Stuff:

#====> Hostname

hostname = socket.gethostname()

#====> OS Version

osversion = platform.platform()

#====> User Name
username = getpass.getuser()

#====> Serial Number
def get_service_tag():
    computer = wmi.WMI("")
    bios_info = computer.Win32_SystemEnclosure()
    for info in bios_info:
        serialnumber = info.SerialNumber
        return serialnumber

getserialnumber = str(get_service_tag())

#====> Free Space

#Get the fixed drives
#wmic logicaldisk get name,description
def freespace():
    drivelist = subprocess.check_output(['wmic', 'logicaldisk', 'get', 'name,description'])
    driveLines = drivelist.split('\n')
    for line in driveLines:
        if line.startswith("Local Fixed Disk"):
            elements = line.split()
            driveLetter = elements[-1]
            free_bytes = ctypes.c_ulonglong(0)
            total_bytes = ctypes.c_ulonglong(0)
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(driveLetter), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
            freespace=free_bytes.value / 1024 /1024 /1024
            freespaceend = freespace  
            return ("{} GB'S ".format(freespaceend)) 
            

def freespaceold():
    free_bytes = ctypes.c_ulong(0)

    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(u'c:\\'), None, None, ctypes.pointer(free_bytes))

    if free_bytes.value == 0:
        print 'dont panic'

    freespace = bfree_bytes.value  
    return freespace

#===> Smart 
def smart():
    proc=subprocess.Popen('wmic diskdrive get status', shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]
    line=output
    if line.startswith("Status"):
        return line[11:57]
#===> Model Number via SYSTEMINFO CMD
def model():

    proc=subprocess.Popen('systeminfo | find "System Model:" ', shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]
    line=output
    #Filter out other info to get the model number
    if line.startswith("System Model:"):
        return line[27:57]

#===> Current Date
now = datetime.datetime.now()
currentdate = str(now)
