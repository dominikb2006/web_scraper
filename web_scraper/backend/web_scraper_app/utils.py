from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse


def is_valid(url):
    """Checks whether `url` is a valid URL."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
    """Returns all image URLs on a single `url`"""
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    urls = []
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def url_into_text(url):
    # get url
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
