import sys

# Functions
from getEmails import getEmails
#from generateWeeklyTrafic import generateWeeklyTraficGraph
from generateTopNSenders import generateTopNSenders
# config variables
from config import username
from config import password
from devConfig import *

print(
    "\n\n-----------Press Enter if you want to skip one of the following filters-----------\n"
)
if sender == 0:
    sender = input("Enter the email adresse of the sender: ")

if beginDate == 0:
    beginDate = input(
        "Enter the begin date of the emails to treat (ex: 01-Aug-2019): ")

if endDate == 0:
    endDate = input(
        "Enter the end date of the emails to treat(ex: 31-Aug-2019):")

if analysis == 0:
    analysis = input("Enter the analysis type(\n1:Remi\n2:David\n3:Alex\n--->")

pandasDataFrameOfEmails = getEmails(
    username, password, 5, sender, beginDate, endDate)
# generateWeeklyTraficGraph(pandasDataFrameOfEmails)
generateTopNSenders(pandasDataFrameOfEmails)
