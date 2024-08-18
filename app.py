from bs4 import BeautifulSoup
from utils import findURL, getHTML


def getResponse(text: str) -> str:
    URL = findURL(text)
    if not URL:
        return
    HTML = getHTML(URL)
    if not HTML:
        return
    preview = getPreview(HTML)
    if not preview:
        return
    return preview


def getPreview(HTML: str) -> str | None:
    soup = BeautifulSoup(HTML, features="html.parser")
    title = getTitle(soup)
    descr = getDescription(soup)
    if title and not descr:
        preview = "**" + title + "**"
    if descr and not title:
        preview = descr
    if title and descr:
        preview = "**" + title + "**" + "\n\n" + descr
    return preview


def getTitle(soup: BeautifulSoup) -> str | None:
    return soup.title.string


def getDescription(soup: BeautifulSoup) -> str | None:
    metas = soup.find_all("meta")
    for meta in metas:
        attrs = meta.attrs
        if "name" in attrs and attrs["name"] == "description":
            return attrs["content"]
