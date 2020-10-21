import ctypes


#Create a handle
user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll") #Error handle

# Windows doc https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxa

hWnd = None
lpText = "Hello World"
lpCaption = "Hello students"
uType = 0x00000001 # The message box contains two push buttons OK and cancel

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

#Implement some error handling, anything above 0 something went wrong
error = k_handle.GetLastError()

if error !=0:
    print("Error Code: (0)".format(error))
    exit(1)

if response ==1:
    print("User clicked OK!")
    



