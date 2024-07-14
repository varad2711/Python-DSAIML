import os
import time
import urllib.error
import urllib.request
import psutil
import urllib
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen("https://216.58.192.142",timeout=1)
        return True
    except urllib.error.URLError as err:
        return False

def MailSender(filename,time):
    try:
        fromaddr="varad.burner@gmail.com"
        toaddr="varad.chaskar.27@gmail.com"
        msg=MIMEMultipart()
        msg['From']=fromaddr
        msg['To']=toaddr
        body = """
        Hi hello Bye%s%s
        """%(toaddr,time)

        Subject="""
        subject%s
        """%(time)

        msg['Subject']=  Subject
        msg.attach(MIMEText(body,'plain'))
        attachment = open (filename,"rb")
        p = MIMEBase('application','ocelet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',"attachment;filename= %s"%filename)

        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(fromaddr,"lmao you tried")
        text = msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        s.quit()
        print("Log file successfully sent through mail")

    except Exception as E:
        print("Unable to send email",E)

def ProcessLog(log_dir = "Marvellous"):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    separator = "-"*80
    log_filename = f"MarvellousLog{time.ctime().replace(' ', '_').replace(':', '_')}.log"
    log_path = os.path.join(log_dir, log_filename)
    f = open(log_path,'w')
    f.write(separator+ "\n")
    f.write("Mar Process logger: "+time.ctime()+"\n")
    f.write(separator+"\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    for element in listprocess:
        f.write("%s\n"%element)

    print("Log file generated at the location %s"%(log_path))

    connceted = is_connected()
    
    if connceted:
        startTime = time.time()
        MailSender(log_path,time.ctime())
        endTime = time.time()
        print("Took %s seconds to send the mail"%(endTime-startTime))
    else:
        print("There is no internet connection")        

def main():
    print("Application Name: "+argv[0])
    if(len(argv)!=2):
        print("Error")
        exit()
    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error: Invalid Datatype")
    except Exception as E:
        print("Error: Exception",E)

if __name__ == "__main__":
    main()