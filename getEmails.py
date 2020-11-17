import imapclient
import imaplib
import smtplib
import pyzmail
import pandas as pd
from getpass import getpass
from pprint import pprint

# config variables
from config import username
from config import password


def getEmails(username, password):
    print(username, password)
    # Ask for credentials
    if username == "" and password == "":
        username = input("Enter user email: ")  # alexandre.girbal.pro@gmail.com
        password = getpass("Enter user password: ")
    print("Fetching emails of ", username, "...")

    imap_server = "imap.gmail.com"
    smtp_server = "smtp.gmail.com"

    imapobj = imapclient.IMAPClient(imap_server, ssl=True)
    imapobj.login(username, password)

    smtpobj = smtplib.SMTP(smtp_server, 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.login(username, password)

    pprint(imapobj.list_folders())

    imaplib._MAXLINE = 10000000

    imapobj.select_folder("Inbox", readonly=True)
    UIDs = imapobj.search(["FROM", "fabienvol@gmail.com"])

    sendersAdresses = []
    receiversAdresses = []
    dates = []
    subjects = []
    contents = []

    for i in range(5):
        raw_message = imapobj.fetch(UIDs[i], ["BODY[]"])
        message = pyzmail.PyzMessage.factory(raw_message[UIDs[i]][b"BODY[]"])

        sendersAdresses.append(message.get_addresses("from"))
        receiversAdresses.append(message.get_addresses("to"))
        dates.append(message.get_decoded_header("date"))
        subjects.append(message.get_subject())
        contents.append(
            message.text_part.get_payload().decode(message.text_part.charset)
        )

    df = pd.DataFrame(
        {
            "sendersAdresses": sendersAdresses,
            "receiversAdresses": receiversAdresses,
            "dates": dates,
            "subjects": subjects,
            "contents": contents,
        }
    )
    df.to_csv(f"outputs/emailsOf{username}.csv", index=False)


getEmails(username, password)