import os
import requests
import re
from text_summary import TextSummary

os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    url = input("Paste url here: ")
    respond = requests.get(url)
    data = respond.text

    article = TextSummary()
    text, title = article.get_paragraph_content(data)
    summary = article.summarize_text(text)
    clean_title = re.sub('\W+', ' ', title)

    print('\033[4m' + title + '\033[0m')
    print(summary)

    # if you want to save the summary into a text file:
    # uncomment the following:
    #with open("{}.txt".format(clean_title[:20].replace(" ", "_")), "w") as f:
    #    f.writelines(title + '\n')
    #    f.writelines('\n')
    #    f.writelines(summary)
