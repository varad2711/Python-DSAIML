import psutil
import os
import time

def CreateLogFile(Foldername = "Logs"):

    starttime = time.time()

    if not os.path.exists(Foldername):
        os.mkdir(Foldername)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" " , "")
    timestamp = timestamp.replace(":" , "_")
    FileName = os.path.join(Foldername , "ProcessLog_%s.log"  %{timestamp})
    
    FileName = os.path.abspath(FileName)

    fd = open(FileName , "w")
    seperator = "-"*70

    fd.write(seperator  + "\n")
    fd.write("Proccess Log " + "\n")
    fd.write("Log file created at : " + time.ctime() + "\n")
    fd.write(seperator  + "\n")

    Arr = GetProcessInfo()
    
    fd.write("Contents of Log File : " + "\n")
    fd.write(seperator  + "\n")

    for data in Arr:
        fd.write("%s \n"  %data)

    print("Log file created")

    endtime = time.time()

    reqTime = endtime - starttime
    print("Required Time for execution : " , reqTime)

    fd.write("Required Time for execution : " +  str(reqTime)  + '\n')

    fd.write(seperator  + "\n")  
    fd.close()

def GetProcessInfo():

    ret = []

    for proc in psutil.process_iter(['pid' , 'name' , 'username']):
        ret.append(proc)

    return ret

def main():

    CreateLogFile()

if __name__ == "__main__":
    main()