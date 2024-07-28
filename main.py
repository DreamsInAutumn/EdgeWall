# -- libraries --

import os
import subprocess
import time
import ctypes
import psutil
import winreg
import json
import sys

# -- classes --

from classes.firewall import Firewall
from classes.messages import Messages

# -- Global variables --

version = "0.3.3"

# -- core functions --

def GetEdgeViewPath():
    #build full edgeview path from registry info: installation path + \ + version + \ + executable
    try:
        key_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Microsoft EdgeWebView"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)

        install_location, _ = winreg.QueryValueEx(key, "InstallLocation")
        version, _ = winreg.QueryValueEx(key, "Version")

        full_path = os.path.join(install_location, version, "msedgewebview2.exe")

        return full_path if os.path.exists(full_path) else None
    except WindowsError:
        return None

def IsProcessRunning(process_name):
    # return True if passed process is running.
    for proc in psutil.process_iter(['name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False

def IsAdmin():
    # return true if running with administrative privileges
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def SkipArg():
    if len(sys.argv) > 1 and sys.argv[1] == "skip":
        return True
    else:
        return False


# -- void functions --

def ScreenClear():
    os.system('cls' if os.name == 'nt' else 'clear')

def RunApp(caller, arg):
    # calls executable with arg
    subprocess.Popen([caller, arg])


# -- procedural functions -- 

def WaitLoad(timeout, msg, exeToDetect):
    # returns true if process is running before timeout, else returns false
    tries = timeout

    msg.WaitRun()
    while not IsProcessRunning(exeToDetect) and tries >= 0:
        msg.AppMessageWaitN(tries)
        tries -= 1
        time.sleep(1)

    if tries <= 0:
        return False
    else:
        return True

def WaitClose(exeToDetect):
    #loop while exe in argument is running
    while IsProcessRunning(exeToDetect):
        time.sleep(1)

def LoadConfig(configFile):
    class Config:
        def __init__(self, exeToDetect: str, winApp: str, fwRule: str, friendlyAppName: str):
            self.exeToDetect = exeToDetect
            self.winApp = winApp
            self.fwRule = fwRule
            self.friendlyAppName = friendlyAppName

    with open('config.json', 'r') as file:
        data = json.load(file)

    config = Config(
        exeToDetect     = data.get('exeToDetect'),
        winApp          = data.get('winApp'),
        fwRule          = data.get('fwRule'),
        friendlyAppName = data.get('friendlyAppName')        
    )

    return config


# -- main function --

def main():
    ScreenClear()

    # load configuration data
    config = LoadConfig('config.json')

    # initialize variables
    appTimeout      = 4
    shell           = "explorer.exe"
    edgeViewPath    = GetEdgeViewPath()

    # initialize classes
    msg             = Messages(config.friendlyAppName)
    EdgeFw          = Firewall(config.fwRule, edgeViewPath)

    # hi    
    msg.Welcome()

    if IsAdmin():
        msg.FwRuleCheck()
        EdgeFw.Delete()
    
        msg.FwAdd()
        EdgeFw.Add()

        # check debug cli argument "skip", load if not equal.
        if not SkipArg():
            RunApp(shell, config.winApp)

        if WaitLoad(appTimeout, msg, config.exeToDetect):
            msg.Running()
            msg.WaitClose()
            WaitClose(config.exeToDetect)
            msg.Closed()
        else:
            msg.ErrLoadFail()

        msg.FwDelete()
        EdgeFw.Delete()

    else:
        msg.ErrPriv()
        input()

    msg.Exit()
    time.sleep(3)


if __name__ == "__main__":
    main()


# the_end
