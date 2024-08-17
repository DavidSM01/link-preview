from bs4 import BeautifulSoup
from utils import searchUrl, getHtml


def getResponse(text: str) -> str:
    url = searchUrl(text)
    if url:
        preview = getPreview(url)
        if preview:
            return preview


def getPreview(url: str) -> str:
    htmlStr = getHtml(url)
    if htmlStr:
        soup = BeautifulSoup(htmlStr, features="html.parser")
        title = getTitle(soup)
        descr = getDescription(soup)
        if title and not descr:
            preview = "**" + title + "**"
        if descr and not title:
            preview = descr
        if title and descr:
            preview = "**" + title + "**" + "\n\n" + descr
    return preview


def getTitle(soup):
    return soup.title.string


def getDescription(soup) -> str:
    metas = soup.find_all("meta")
    for meta in metas:
        attrs = meta.attrs
        if "name" in attrs and attrs["name"] == "description":
            return attrs["content"]
