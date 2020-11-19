import sys
import pandas as pd

# Functions
from getEmails import getEmails

from analysis.generateWeeklyTrafic import generateWeeklyTraficGraph
from analysis.generateTopNSenders import generateTopNSenders
from analysis.generateCloudWord import generateCloudWord

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
    analysis = input(
        "Enter the analysis type \n1:Remi\n2:Top N Senders\n3:Weekly trafic graph\n--->"
    )

try:
    pandasDataFrameOfEmails = pd.read_csv(f"./outputs/emailsOf{username}.csv")
except:
    pandasDataFrameOfEmails = getEmails(
        username, password, -1, sender, beginDate, endDate
    )

if analysis == 1:
    generateCloudWord(pandasDataFrameOfEmails)
if analysis == 2:
    generateTopNSenders(pandasDataFrameOfEmails)
if analysis == 3:
    generateWeeklyTraficGraph(pandasDataFrameOfEmails)
