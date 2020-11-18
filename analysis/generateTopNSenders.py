import matplotlib.pyplot as plt
from pprint import pprint
from datetime import datetime
import pandas as pd


def generateTopNSenders(dataFrame):

    sender_top_20 = dataFrame['sendersAdresses'].value_counts().nlargest(20)
    sender_top_20_count = sender_top_20.values
    sender_top_20_names = sender_top_20.index.tolist()
    sendersAdresses = []
    for i in range(len(sender_top_20_names)):
        sendersAdresses.append(''.join(sender_top_20_names[i][0]))
        print(''.join(sender_top_20_names[i][0]))

    print(sender_top_20_count)
    print(sendersAdresses)
    plt.figure()
    plt.barh(sendersAdresses, sender_top_20_count,
             color='forestgreen', ec='black', linewidth=1)
    plt.gca().invert_yaxis()
    plt.title('Top 20 Senders', fontsize=14, fontweight='bold')
    plt.xlabel('Received Email Count', fontweight='bold')
    plt.tight_layout()
    plt.savefig("./outputs/topNSenders.png")
