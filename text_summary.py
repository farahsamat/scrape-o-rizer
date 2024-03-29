from gensim.summarization import summarize
from bs4 import BeautifulSoup


class TextSummary:
    def __init__(self):
        return

    def get_paragraph_content(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        title = soup.find('title').string
        paragraph = [p.getText() for p in soup.find_all('p')]
        whole_text = ' '.join(paragraph)
        return whole_text, title

    def summarize_text(self, text):
        return summarize(text, word_count=150)


