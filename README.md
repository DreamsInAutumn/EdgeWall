# EdgeWall

	Notes

        Apps* use edgeview to load ads.

        Objective:
	    Create a firewall rule that blocks all outbound comms for edgeview
            Run app
            Wait until it closes
            Delete the edgeview Firewall Rule
            Exit

        Observations
            After using the app with a permanent Rule, simply enabling and disabling the rule when needed, it was observed that
            the rule was being deleted after a period of days.

            My theory is that MS consider edgeview to be a core component of windows functionality, and that Firewalling it is an issue.
            To get around this, we delete and recreate the temporary rule each time this App is run

        Warning
            Closing this app directly will prevent any edgeview dependent app from having net access (weather mail etc)
            It will clean up the firewall rules on its next launch.
