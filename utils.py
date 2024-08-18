import re
import requests


def findURL(text: str) -> str | None:
    regex = "(http[s]?)://([-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b)([-a-zA-Z0-9@:%._\\+~#?&//=]*)"
    match = re.search(regex, text, re.MULTILINE)
    if match:
        return match[0], match[1], match[2], match[3]


def getHTML(url: str) -> str | None:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    headers = resp.headers
    contentType = headers["content-type"]
    isHTML = re.search("text/html", contentType)
    if isHTML:
        resp.encoding = "utf8"
        HTML = resp.text
        if HTML:
            return HTML
