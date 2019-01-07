import collections
import logging
from urllib.parse import urlsplit, unquote, urljoin

import requests
from lxml import html


logger = logging.getLogger(__name__)


def find_recursive(url, xpath, xpath_url="//a/@href", ignore=None, accept=None, cookies=None):
    urls = collections.deque([url])
    viewed = {url}
    s = urlsplit(url)
    base_url = f"{s.scheme}://{s.netloc}"
    while urls:
        logger.debug("enqued: %d, viewed: %d", len(urls), len(viewed))
        url = urls.popleft()
        if ignore and url in ignore:
            logger.debug("ignore url %s: present in ignore list", url)
            continue
        if accept and url not in accept:
            logger.debug("ignore url %s: not present in accept list", url)
            continue
        try:
            r = requests.get(url, cookies=cookies, headers={"User-agent": "Mozilla/5.0"})
            r.raise_for_status()
        except requests.RequestException:
            logger.debug("ignore url %s: failed to retrieve", url, exc_info=True)
            continue
        try:
            parsed = html.fromstring(r.text)
        except Exception:
            logger.debug("ignore url %s: failed to parse", url, exc_info=True)
            continue
        for new_url in parsed.xpath(xpath_url):
            if not new_url:
                continue
            # TODO: check new_url is not cross domain link
            new_url = urljoin(base_url, unquote(new_url))
            viewed.add(new_url)
            if base_url in new_url:
                urls.append(new_url)
            logger.info("add url %s", new_url)
        yield from parsed.xpath(xpath)
