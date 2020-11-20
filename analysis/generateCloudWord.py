import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from personalStopword import personalStopword
import re


def generateCloudWord(dataFrame):
    print("Generating word cloud graph ...")
    # Dowload stopwords list
    nltk.download("stopwords")
    stop = stopwords.words("french")

    # Create a list of words
    text = ""

    # Remove urls
    dataFrame["contents"] = dataFrame["contents"].apply(
        lambda x: re.split("https:\/\/.*", str(x))[0]
    )

    # Remove the "*"
    dataFrame["contents"] = dataFrame["contents"].apply(
        lambda x: re.split("\*", str(x))[0]
    )

    # Remove dowloaded stopwords
    dataFrame["contentsWithoutStop"] = dataFrame["contents"].apply(
        lambda x: " ".join([word for word in x.split() if word.lower() not in (stop)])
    )

    # Remove personals stopwords
    dataFrame["contentsWithoutStop"] = dataFrame["contentsWithoutStop"].apply(
        lambda x: " ".join(
            [word for word in x.split() if word.lower() not in (personalStopword)]
        )
    )

    # Create the words list
    for item in dataFrame["contentsWithoutStop"]:
        if isinstance(item, str):
            text += " " + item

        # Replace few caracters
        text.replace("'", "")
        text.replace("*", "")
        text.replace("-", "")
        text.replace(",", "")
        text.replace('"', "")

    # Create the wordcloud
    wordcloud = WordCloud(width=800, height=800, background_color="white")
    wordcloud.generate(text)
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.title("Most Used Words in your content mails", fontsize=20, ha="center", pad=20)
    plt.show()
