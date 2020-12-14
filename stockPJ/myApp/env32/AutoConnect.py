from pywinauto import application
import os, time

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')

def getPwd():
    with open ('C:\\myKey\\creon.txt') as f:
        pw = f.readline()
    return pw.strip()

time.sleep(5)
app = application.Application()
app.start(getPwd())