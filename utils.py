import re
import requests


def searchUrl(text: str):
    regex = "((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)"
    search = re.search(regex, text, re.MULTILINE)
    if search and search[0]:
        return search[0]


def getHtml(url: str) -> str:
    resp = requests.get(url, timeout=8)
    status = resp.status_code
    if status == requests.codes.ok:
        resp.encoding = "utf8"
        html = resp.text
        if html:
            return html
    else:
        raise InvalidStatus("Page could not be loaded, error " + str(status))


class InvalidStatus(Exception):
    "Response with bad status code"
