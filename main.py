from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from requests_html import HTMLSession
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

internal_urls = []
external_urls = []
pr_urls = {}
ref = {}

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_url_on_page(url):
    urls = set()
    list = []
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in internal_urls:
            internal_urls.append(href)
            list.append(href)
            ref[url] = list
            continue
        if domain_name not in href:
            if href not in external_urls:
                external_urls.append(href)
                list.append(href)
                ref[url] = list
            continue
        urls.add(href)
        list.append(href)
        ref[url] = list
        internal_urls.append(href)
    return urls


def get_page_rank(url, d):
    previous_result = 0
    pr_links = 0

    tarr = []
    for t in ref:
        for k in ref[t]:
            if url == k:
                if t != url:
                    tarr.append(t)
    ref_to = set(tarr)

    for tl in ref_to:
        if pr_urls.get(tl):
            if internal_urls.count(tl):
                pr_links += pr_urls.get(tl) / internal_urls.count(tl)
            else:
                pr_links += pr_urls.get(tl) / 1
        else:
            if internal_urls.count(tl):
                pr_links += 1 / internal_urls.count(tl)
                pr_links += 1

    if pr_urls.get(url):
        previous_result = pr_urls.get(url)

    pr_link = (1 - d) + d * pr_links
    pr_urls[url] = pr_link

    # print(pr_link)

    if abs(previous_result - pr_urls.get(url)) < 0.00000001:
        return -1

    return 0

url = 'https://shop.bmthofficial.com/'
links = get_url_on_page(url)

for link in links:
    get_url_on_page(link)

# print(Counter(internal_urls))

# ranks = Counter(internal_urls).items()

ranks = set(internal_urls)

# page_ranks = [item for item, count in Counter(internal_urls).items() if count >= 1]

n = 0
flag = True
while(flag):
    get_page_rank(url, 0.5)
    for rank in ranks:
        if get_page_rank(rank, 0.5) == -1:
            flag = False
            break
    n += 1
    if n > 666:
        flag = False

print('Count of steps: ' + str(n))

# result_ranks = {}
#
# for rank in links:
#     # print('url: ' + rank)
#     # print('page rank: ' + str(pr_urls.get(rank)))
#     result_ranks[rank] = pr_urls.get(rank)
#
# result = set(result_ranks)
#
# for r in result:
#     print('url: ' + r)
#     print('page rank: ' + str(result_ranks.get(r)))

tarr = []
for tl in links:
    tarr.append([url.replace(url, '/') + ' PR(' + str('{:3.3f}'.format(pr_urls.get(url))) + ')', tl.replace(url, '/') + ' PR(' + str('{:3.3f}'.format(pr_urls.get(tl))) + ')'])
    for t in ref:
        for k in ref[t]:
            if tl == k:
                if t != tl:
                    if t not in tarr:
                        tarr.append([tl.replace(url, '/') + ' PR(' + str('{:3.3f}'.format(pr_urls.get(tl))) + ')', t.replace(url, '/') + ' PR(' + str('{:3.3f}'.format(pr_urls.get(t))) + ')'])

# for ttta in tarr:
#     print(ttta)

plt.figure(figsize=(19.2, 10.8))
df = pd.DataFrame(tarr, columns=["from", "to"])
GA = nx.from_pandas_edgelist(df, source="from", target="to")
#pos = nx.spring_layout(GA, k=0.7, scale=0.05)
nx.draw(GA, with_labels=True)
axis = plt.gca()
axis.set_xlim([1.15*x for x in axis.get_xlim()])
axis.set_ylim([1.15*y for y in axis.get_ylim()])
plt.savefig(url.replace('/', '').replace(':', '.') + '.png')
plt.show()
