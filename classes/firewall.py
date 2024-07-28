# -- libraries --
import subprocess

#-- class definition --

class Firewall:
    def __init__(self, rule, appPath):
        self.rule = rule
        self.appPath = appPath

# -- class methods --

    def RuleExists(self) -> bool:
        #Check if the firewall rule exists.
        try:
            result = subprocess.run(["netsh", "advfirewall", "firewall", "show",\
                "rule",\
                f"name={self.rule}"],\
                capture_output=True, text=True, check=True)
            return self.rule in result.stdout
        except subprocess.CalledProcessError:
            return False

    def Add(self):
        #Add firewall rule
        subprocess.run(["netsh","advfirewall", "firewall", "add",\
            "rule",\
            f"name={self.rule}",\
            "protocol=ANY",\
            "dir=out",\
            "action=block",\
            "enable=yes",\
            f"program={self.appPath}"])

    def Delete(self):
        #Remove the firewall rule if it exists.
        if self.RuleExists():
            subprocess.run(["netsh", "advfirewall", "firewall", "delete",\
            "rule",\
            f"name={self.rule}"
        ])
            