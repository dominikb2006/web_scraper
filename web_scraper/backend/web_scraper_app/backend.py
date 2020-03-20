from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm
from urllib.parse import urljoin, urlparse


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
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
        urls.append(img_url)
    return urls


def download(url):
    buffer_size = 1024
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = url.split("/")[-1]
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B",
                    unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


def urlIntoText_Test(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    txt = soup.get_text()
    return txt


def urlIntoText(url):
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
