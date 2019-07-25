#!/usr/bin/python
#
##########################################################################
#
# ABOUT THIS PROGRAM
# extension attribute
# Is Triple Triangle are installed for InDesign 
#
# Check the InDesign Plug-ins folders for TripleTriangle
# Will Pierce
# 20170125
# 2019 07 23
# Updated to find installed versons and report
##########################################################################
# Import modules to help
import os, glob, json
# Create variable to find all of the installed versions of InDesign
installedInDesign = glob.glob('/Applications/Adobe InDesign CC*')
# Check to see if any version of InDesign is installed and if so continue, if not set result and quit
if not installedInDesign:
    print "<result>InDesign NOT installed</result>"
    quit()
else:
    pass
# Create empty dictnatory for the results
result={}
# Loop through the installed versions and check to see if the TripleTriangle plug in is installed
for versions in installedInDesign:
    # Create variable for the TripleTriangle plug in path
    ttPath = os.path.join(versions, 'Plug-Ins', 'TripleTriangle', 'TTShared.InDesignPlugin')
    # Check to see if TripleTriangle plug in is installed
    if os.path.isdir(ttPath):
        # If TripleTriangle plug in found add Yes entry to dictnatory
        result[ versions ] = "Yes"
    else:
        # If TripleTriangle plug in found add No entry to dictnatory
        result[ versions ] = "No"
# Output for JAMF PRO EA
print "<result>"
stringResult=json.dumps(result ).replace("/Applications/Adobe", "").strip('{},"')
print stringResult.strip('\ \"').replace('"', '')
print "</result>"