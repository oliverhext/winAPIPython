
# Function Library : https://docs.python.org/3/library/ctypes.html
# https://github.com/python/cpython/blob/master/Lib/ctypes/wintypes.py
import ctypes
# FindWindowA
# GetWindowThreadProcessId
# OpenProcess
# TerminateProcess



# FindWindowA

# Type LPCSTR is a pointer to a const string (LP means Long Pointer)
# HWND FindWindowA(
#  LPCSTR lpClassName,
#  LPCSTR lpWindowName
# );
# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-findwindowa

k_handle = ctypes.WinDLL("Kernel32.dll")
u_handle = ctypes.WinDLL("User32.dll")

# Access Rights
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)


#c_char_p is a character pointer.  Need to encode because it is ANSI NOT ASCII
#The winuser.h header defines FindWindow as an alias which automatically selects the ANSI or Unicode version hence
#the encode to utf-8

lpWindowName = ctypes.c_char_p(input("Enter Window Name to Kill:").encode('utf-8'))
print(lpWindowName)

# Grap the findWindow handle that gets returned
hWnd = u_handle.FindWindowA(None, lpWindowName)

if hWnd == 0:
    print("Error Code: {0} - Could not grab handle".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Got handle..")
    
# GetWindowThreadProcessId

# DWORD GetWindowThreadProcessId(
# HWND    hWnd,
# LPDWORD lpdwProcessId
# );

# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid
# LPDWORD our DWORD is DWORD = ctypes.c_ulong

lpdwProcessId = ctypes.c_ulong()

response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))

if response == 0:
    print("Error Code: {0} - Could not grab PID".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Got the PID!")


# OpenProcess

# HANDLE OpenProcess(
# DWORD dwDesiredAccess,
# BOOL  bInheritHandle,
# DWORD dwProcessId
# );

# https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess

dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = lpdwProcessId

# TerminateProcess

# BOOL TerminateProcess(
# HANDLE hProcess,
# UINT   uExitCode
# );


hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

if hProcess <= 0:
    print("Error Code: {0} - Could not grab PID".format(k_handle.GetLastError()))
else:
    print("Got our Handle...")
    
# Terminate the process assuming we have persmission to do so.  Run as administrator to test

uExitCode = 0x1
response = k_handle.TerminateProcess(hProcess, uExitCode)

if response ==0:
    print("Error Code: {0} - Could not grab PID".format(k_handle.GetLastError()))
else:
    print("Process terminated......")
