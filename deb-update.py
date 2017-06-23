#!/usr/bin/python

#A simple Update/Upgrade python script for Debian.

import os
import sys, traceback
import time

print ""
print "Dev: Nathan Smith"
print ""

#Options
print "~~~~~~~~~~~~~~~~~~~~~~~"
print "Update/Upgrade Debian"
print "~~~~~~~~~~~~~~~~~~~~~~~"
print "(1) System Update"
print "(2) System Upgrade"
print "(3) Distribution Upgrade"
print "(4) Exit"
print ""

choice = raw_input ("Please Select an Option: ")
if choice == "1":
	print "System Update Selected, Please Wait..."
	time.sleep(5)
	cmd1 = os.system ("sudo apt-get update")
	print ""
	print "System Update Complete"
	print ""
elif choice == "2":
	print "System Upgrade Selected, Please Wait..."
	time.sleep(5)
	cmd1 = os.system ("sudo apt-get upgrade -y")
	print ""
	print "System Upgrade Complete"
	print ""
elif choice == "3":
	print "Distribution Upgrade Selected, Please Wait..."
	time.sleep(5)
	cmd1 = os.system ("sudo apt-get dist-upgrade -y")
	print ""
	print "Distribution Upgrade Complete"
	print ""
elif choice == "4":
	print ""
	print "Goodbye, Have a nice day :)"
	print ""
	sys.exit(0)

