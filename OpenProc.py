import ctypes
# Grab a handle to kernal32.dll

k_handle = ctypes.WinDLL("Kernel32.dll")

# Win API Call
# HANDLE OpenProcess(
# DWORD dwDesiredAccess,
# BOOL bInheritHandle,
# DWAORD dwProcessId
# );

# Access Rights
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

#Setting up the Params
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False

#Trying to get the user to enter the process ID having issues converting to HEX and calling the handle
#processID = int(input("Please enter the process ID in decimal:"))
#dwProcessId = hex(processID)[2:]
#convertID = int(dwProcessId, 0)
#print(convertID)
#print("The process id is: " + dwProcessId)

#Manual input of process id

dwProcessId = 0x364c #Use task manager to show the process to poke at.  Convert PID from dec to hex
print("The processID",dwProcessId)
print("The variables type is:",type(dwProcessId))

#Calling the Windows API Call
response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
print(response)

#Checking for error
error = k_handle.GetLastError()

if error !=0:
    print("Error code :{0}".format(error))
    exit(1)

if response <=0:
    print("Handle was not created")
else:
    print("Handle was Created")


