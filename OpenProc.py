import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll")

PROCESS_AL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

dwDesiredAcess = PROCESS_ALL_ACCESS
dInheritHandle = False
dsProcessId 0x= #Use task manager to show the process to poke at.  Convert PID dec to hex