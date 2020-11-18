import matplotlib.pyplot as plt
from pprint import pprint
from datetime import datetime
import pandas as pd


def generateTopNSenders(dataFrame):
    pprint(dataFrame)
    sender_top_20 = dataFrame['sendersAdresses'].value_counts().nlargest(20)
    sender_top_20_count = sender_top_20.values
    sender_top_20_names = sender_top_20.index.tolist()
    print(sender_top_20_count)
    print(sender_top_20_names)
    plt.figure()
    plt.barh(sender_top_20_names, sender_top_20_count,
             color='forestgreen', ec='black', linewidth=1)
    plt.gca().invert_yaxis()
    plt.title('Top 20 Senders', fontsize=14, fontweight='bold')
    plt.xlabel('Received Email Count', fontweight='bold')
    plt.tight_layout()
