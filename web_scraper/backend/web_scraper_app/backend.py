import requests
from bs4 import BeautifulSoup


def urlIntoText_Test(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    txt = soup.get_text()
    return txt

def urlIntoText(url):
    #get url
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    # remove all javascript and stylesheet code
    for script in soup(["script", "style"]):
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = []
    for line in text.splitlines():
        lines.append(line.strip())
    # break multi-headlines into a line each
    chunks = []
    for line in lines:
        for phrase in line.split("  "):
            chunks.append(phrase.strip())
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    # print(text)
    return text