# -- libraries --
import sys

#-- class definition --

class Messages:
    def __init__(self, friendlyAppName):
        self.friendlyAppName     = friendlyAppName
        self.msgWelcome          = f"Advertising free {self.friendlyAppName}\n-------------------------------------\n"
        self.msgExit             = "Exiting..."
        self.msgGetEdgePath      = f"Getting Edge View Path\n"
        self.msgFwRuleCheck      = f"Checking for old Rules"
        self.msgFwAdd            = "\nAdding firewall rule"
        self.msgFwDelete         = "Deleting firewall rule"
        self.msgWaitRun          = f"Waiting until {self.friendlyAppName} is running...\n"
        self.msgRunning          = f"\n\n{self.friendlyAppName} is running\n"
        self.msgWaitClose        = f"Waiting until {self.friendlyAppName} is closed...\n"
        self.msgClosed           = f"{self.friendlyAppName} is no-longer running\n"
        self.msgErrPriv          = "\nElevated privileges are required \nPress Enter to Continue"
        self.msgErrLoadFail      = f"\n\n{self.friendlyAppName} Failed to load\n"

# -- class methods --

    def AppMessageWaitN(self, message): # no new line
        sys.stdout.write(f'\rWaiting {message}...')
        sys.stdout.flush()  # Flush the output to ensure it's displayed immediately

    def Welcome(self):
            print(self.msgWelcome)

    def Exit(self):
            print(self.msgExit)

    def GetEdgePath(self):
            print(self.msgGetEdgePath)

    def FwRuleCheck(self):
            print(self.msgFwRuleCheck)

    def FwAdd(self):
            print(self.msgFwAdd)

    def FwDelete(self):
            print(self.msgFwDelete)

    def WaitRun(self):
            print(self.msgWaitRun)

    def Running(self):
            print(self.msgRunning)

    def WaitClose(self):
            print(self.msgWaitClose)

    def Closed(self):
            print(self.msgClosed)

    def ErrPriv(self):
            print(self.msgErrPriv)

    def ErrLoadFail(self):
            print(self.msgErrLoadFail)
            