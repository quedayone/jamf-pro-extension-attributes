#!/bin/bash
#####################################################################################################
#
# ABOUT THIS PROGRAM
# extension attribute
# SaveHollywood.saver installed Yes No
#
####################################################################################################
#
# HISTORY
#
#	Version: 1.0
#	- Will Pierce 2019 05 02
#
####################################################################################################
#
# Check to see if SaveHollywood.saver exists
if [ -e /Library/Screen\ Savers/SaveHollywood.saver ]; then 
	result="Yes"
else
	result="No"
fi
#
echo "<result>$result</result>"
exit 0