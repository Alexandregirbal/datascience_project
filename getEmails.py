import imapclient
import imaplib
import smtplib
import pyzmail
import pandas as pd
import re
from getpass import getpass
from pprint import pprint
from datetime import date

from config import username
from config import password


def deleteForwardedMessagesFromMessage(message: str):
    nextMessage = re.split(r"\n.*[\,].*\<\s*.*>", message)[0]
    return nextMessage


def getEmails(
    username,
    password,
    limit=-1,
    sender="",
    beginDate="",
    endDate="",
    imap_server="imap.gmail.com",
    smtp_server="smtp.gmail.com",
):
    # Ask for credentials if needed
    if username == "" and password == "":
        username = input("Enter user email: ")
        password = getpass("Enter user password: ")
    print("Fetching emails of ", username, "...")

    imapobj = imapclient.IMAPClient(imap_server, ssl=True)
    imapobj.login(username, password)

    smtpobj = smtplib.SMTP(smtp_server, 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.login(username, password)

    imaplib._MAXLINE = 10000000

    imapobj.select_folder("Inbox", readonly=True)
    conditions = []
    if sender != "":
        print(sender)
        conditions.append("FROM")
        conditions.append(sender)

    if beginDate != "":
        print("beginDate" + beginDate)
        conditions.append("SINCE")
        conditions.append(beginDate)

    if endDate != "":
        print("endDate" + endDate)
        conditions.append("BEFORE")
        conditions.append(endDate)
    print(conditions)
    UIDs = imapobj.search(conditions)
    sendersAdresses = []
    receiversAdresses = []
    dates = []
    days = []
    subjects = []
    contents = []

    if limit != -1:
        numberOfIterations = limit
    else:
        numberOfIterations = len(UIDs)
    for i in range(numberOfIterations - 1):
        raw_message = imapobj.fetch(UIDs[i], ["BODY[]"])
        message = pyzmail.PyzMessage.factory(raw_message[UIDs[i]][b"BODY[]"])

        sendersAdresses.append(message.get_addresses("from"))
        receiversAdresses.append(message.get_addresses("to"))
        dates.append(message.get_decoded_header("date"))
        days.append(message.get_decoded_header("date").split(",")[0])
        subjects.append(message.get_subject())
        newmessage = deleteForwardedMessagesFromMessage(
            message.text_part.get_payload().decode(message.text_part.charset)
        )
        contents.append(newmessage)

    df = pd.DataFrame(
        {
            "sendersAdresses": sendersAdresses,
            "receiversAdresses": receiversAdresses,
            "days": days,
            "dates": dates,
            "subjects": subjects,
            "contents": contents,
        }
    )
    df.to_csv(f"outputs/emailsOf{username}.csv", index=False)
    print("Data fetched, csv written with success.")
    return df
