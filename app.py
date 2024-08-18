from bs4 import BeautifulSoup
from utils import findURL, getHTML


def getResponse(text: str) -> str:
    [URL, protocol, domain, rest] = findURL(text)
    print(URL, protocol, domain, rest)
    if not URL:
        return
    HTML = getHTML(URL)
    if not HTML:
        return
    preview = getPreview(HTML, protocol, domain)
    if not preview:
        return
    return preview


def getPreview(HTML: str, protocol: str, domain: str) -> str | None:
    soup = BeautifulSoup(HTML, features="html.parser")
    title = getTitle(soup)
    descr = getDescription(soup)
    iconURL = findIconURL(soup, protocol, domain)
    # icon = getIcon(iconURL)
    print(iconURL)
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


def findIconURL(soup: BeautifulSoup, protocol: str, domain: str) -> str:
    iconLink = soup.find("link", rel="shortcut icon")
    if not iconLink:
        iconLink = soup.find("link", rel="icon")
    if not iconLink:
        return protocol + "://" + domain + "/favicon.ico"
    if iconLink and iconLink["href"]:
        return iconLink["href"]


def getIcon(iconURL: str):
    pass
