import ctypes


#Create a handle
user_handle = ctypes.WinDLL("User32.dll")#Message box uses User32.dll
k_handle = ctypes.WinDLL("Kernel32.dll") #Error handle

# Creates a simple message box
# Windows doc https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxa
#Message box function

hWnd = None
lpText = u"Hello World"
lpCaption = u"Hello students" # Notice the u before the string to send as unicode
uType = 0x00000001 # The message box contains two push buttons OK and cancel. See webpage above for other options

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

#Implement some error handling, anything above 0 something went wrong
error = k_handle.GetLastError()

if error !=0:
    print("Error Code: (0)".format(error))
    exit(1)

if response ==1:
    print("User clicked OK!")
elif response ==2:
    prinf("User clicked cancel")
    
    
    



