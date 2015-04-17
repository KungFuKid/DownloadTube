import sys
import common_fun
import ctypes


TH32CS_SNAPPROCESS = 0x00000002
class PROCESSENTRY32(ctypes.Structure):
     _fields_ = [("dwSize", ctypes.c_ulong),
                 ("cntUsage", ctypes.c_ulong),
                 ("th32ProcessID", ctypes.c_ulong),
                 ("th32DefaultHeapID", ctypes.c_ulong),
                 ("th32ModuleID", ctypes.c_ulong),
                 ("cntThreads", ctypes.c_ulong),
                 ("th32ParentProcessID", ctypes.c_ulong),
                 ("pcPriClassBase", ctypes.c_ulong),
                 ("dwFlags", ctypes.c_ulong),
                 ("szExeFile", ctypes.c_char * 260)]


def killPid(pid):
    print( pid )
    handle = ctypes.windll.kernel32.OpenProcess(1, False, pid)
    ctypes.windll.kernel32.TerminateProcess(handle,0)

def FindADBProcess( filePath ):
    pidlist = []
    for line in open( filePath ):
        v = line.split( ' ' )
        pid = v[-1]
        pid = pid.replace( '\n' , '' )
        #print(pid )
        if pid !='0' and pid not in pidlist:
            pidlist.append( pid )
    #print( pidlist )

    for pid in pidlist:

       CreateToolhelp32Snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot
       Process32First = ctypes.windll.kernel32.Process32First
       Process32Next = ctypes.windll.kernel32.Process32Next
       CloseHandle = ctypes.windll.kernel32.CloseHandle

       hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
       pe32 = PROCESSENTRY32()
       pe32.dwSize = ctypes.sizeof(PROCESSENTRY32)
       if Process32First(hProcessSnap,ctypes.byref(pe32)) == False:
          print("Failed getting first process.", file=sys.stderr)
          return
       while True:

          i_pid = int( pid )
          if i_pid == pe32.th32ProcessID:
              exefileName = str(pe32.szExeFile, encoding = "utf-8")  
              if  exefileName!= 'studio64.exe':
                  print( exefileName )
                  killPid( pe32.th32ProcessID)
          
          if Process32Next(hProcessSnap,ctypes.byref(pe32)) == False:
             break
       CloseHandle(hProcessSnap)
        

if(__name__=='__main__'):

    command = sys.argv[1]
    if command == "find":
        FindADBProcess( sys.argv[2] )
