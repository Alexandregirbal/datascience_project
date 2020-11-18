import matplotlib.pyplot as plt
import pandas as pd


def generateWeeklyTraficGraph(dataFrame):
    print("Generating weekly trafic graph ...")
    dataFrame["days"] = pd.Categorical(
        dataFrame["days"],
        categories=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        ordered=True,
    )

    # sort by day of the week
    count_sorted_by_day = dataFrame["days"].value_counts().sort_index()
    print(count_sorted_by_day)
    plt.figure()
    count_sorted_by_day.plot(marker="o", color="blue", linewidth=2, ylim=[0, 20])
    plt.title("Weekly Email Traffic", fontweight="bold", fontsize=14)
    plt.ylabel("Received Email Count", fontweight="bold", labelpad=15)
    plt.grid()
    plt.savefig("./outputs/weeklyTrafic.png")