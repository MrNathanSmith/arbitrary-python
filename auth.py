#!/usr/bin/python

import os
import sys

print ""
print "A Simple Authentication Script"
print ""

#Authentication
password = "qwerty"
typepwd = raw_input("Please enter password: ")
print "____________________________________"
if password == typepwd:
	print ""
	print "Login Successful"
	print ""
	print "Welcome, Admin"
	print ""

else:
	print ""
	print "Access Denied!"
	print ""
sys.exit(0)

