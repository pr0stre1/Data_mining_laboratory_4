from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from requests_html import HTMLSession
from collections import Counter

"""
dict_ranks = {}
dict_count = {}

def is_valid(url):
    Checks whether `url` is a valid URL.
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    Returns all URLs that is found on `url` in which it belongs to the same website
    # all URLs of `url`
    # urls = []

    internal_urls = []
    # external_urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    #req = Request(url)
    #html_page = urlopen(req)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        # if href == "" or href is None:
            # print('href empty tag')

        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if not is_valid(href):
            print('not a valid URL')
        else:
            if href in internal_urls:
                print('already in the set')
            else:
                if domain_name not in href:
                    print('external link')
                else:
            # external link
            # if href not in external_urls:
                # print(f"[!] External link: {href}")
                # external_urls.add(href)
        # print(f"[*] Internal link: {href}")
        #    urls.append(href)
                    if href in internal_urls:
                        print('already in set')
                    else:
                        internal_urls.append(href)

    return internal_urls


def jacobi(A, b, eps, N=25, x=None):
    # Solves the equation Ax=b via the Jacobi iterative method.
    # Create an initial guess if needed
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times
    for i in range(N):
        x = (b - dot(R, x)) / D

    return x


def initialize_ranks(url):
    dict_ranks = {}

    for sub_link in get_all_website_links(url):
        dict_ranks[sub_link] = eval("1")

    return dict_ranks


def get_page_rank(url, d, links):
    global dict_ranks, dict_count
    pr_links = 0

    for url in links:
    #     sub_sub_link = len(get_all_website_links(sub_link))
    #     if sub_sub_link:
    #        if dict_ranks.get(sub_link):
    #            pr_links += dict_ranks.get(sub_link) / len(sub_sub_link)
    #        else:
    #            pr_links += 1
        if dict_ranks.get(href):
            pr_links = pr_links + (float(dict_ranks.get(href)) / float(dict_count.get(href)))
        else:
            pr_links += 1

    pr_link = (1 - d) + d * pr_links

    dict_ranks[url] = pr_link

    # print('link ' + url + ' pr ' + str(pr_link))

    return dict_ranks


link = 'http://imgur.com/'
links = get_all_website_links(link)
sub_link = []
ref = [sub_link]

array_of_links = []
array_of_links.clear()

print(links)

# for i in links:
#     temp = get_all_website_links(i)
#     for j in temp:
#         array_of_links.append(j)
#         # links.append(j)
#
# for value in array_of_links:
#     print(value)
#     print(array_of_links.count(value))

# count = []
# for i in links:
#     for element in all:
#         if element == links[i]:
#             sub_link.append(element)
#             ref.insert(i, sub_link)
#     sub_link = []
# for i in ref:
#     print(len(i))
# link_ranks = initialize_ranks(link)
# dict_count[link] = count
# rank = 0
# # links = get_all_website_links(link)
# # link_count[link] = len(links)
#
# for t in links:
#     count = 0
#     for i in sub_link:
#         for j in i:
#             if j == t:
#                 count += 1
#     for b in links:
#         if t == b:
#             count += 1
#
#     dict_count[t] = count
#
# print(dict_count)
#
# for i in range(666):
#     dict_ranks = get_page_rank(link, 0.5, links)
#
#     if (abs(float(dict_ranks.get(link)) - rank)) < 0.000001:
#         break
#
#     rank = float(dict_ranks.get(link))
#     for href in links:
#         dict_ranks = get_page_rank(href, 0.5, links)
#
# print(dict_ranks)
"""

# internal_urls = set()
# external_urls = set()
#
# total_urls_visited = 0
#
# def is_valid(url):
#     """
#     Checks whether `url` is a valid URL.
#     """
#     parsed = urlparse(url)
#     return bool(parsed.netloc) and bool(parsed.scheme)
#
# def get_all_website_links(url):
#     urls = set()
#     domain_name = urlparse(url).netloc
#     session = HTMLSession()
#     response = session.get(url)
#     try:
#         response.html.render()
#     except:
#         pass
#     soup = BeautifulSoup(response.html.html, "html.parser")
#     for a_tag in soup.findAll("a"):
#         href = a_tag.attrs.get("href")
#         if href == "" or href is None:
#             continue
#         href = urljoin(url, href)
#         parsed_href = urlparse(href)
#         href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
#         if not is_valid(href):
#             continue
#         if href in internal_urls:
#             continue
#         if domain_name not in href:
#             if href not in external_urls:
#                 external_urls.add(href)
#             continue
#         urls.add(href)
#         internal_urls.add(href)
#     return internal_urls
#
# internal = []
#
# for element in (get_all_website_links('https://www.google.com/')):
#     for link in (get_all_website_links(element)):
#         internal.append(link)
#
# print(Counter(internal))

# import requests
# from bs4 import BeautifulSoup
#
# # initialize the set of links (unique links)
# internal_urls = set()
# external_urls = set()
#
# total_urls_visited = 0
#
#
# def is_valid(url):
#     """
#     Checks whether `url` is a valid URL.
#     """
#     parsed = urlparse(url)
#     return bool(parsed.netloc) and bool(parsed.scheme)
#
#
# def get_all_website_links(url):
#     urls = set()
#     domain_name = urlparse(url).netloc
#     soup = BeautifulSoup(requests.get(url).content, "html.parser")
#     for a_tag in soup.findAll("a"):
#         href = a_tag.attrs.get("href")
#         if href == "" or href is None:
#             continue
#         href = urljoin(url, href)
#         parsed_href = urlparse(href)
#         href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
#         if not is_valid(href):
#             continue
#         if href in internal_urls:
#             # already in the set
#             continue
#         if domain_name not in href:
#             if href not in external_urls:
#                 external_urls.add(href)
#             continue
#         urls.add(href)
#         internal_urls.add(href)
#     return urls
#
#
# def crawl(url, max_urls=50):
#     global total_urls_visited
#     total_urls_visited += 1
#     links = get_all_website_links(url)
#     for link in links:
#         if total_urls_visited > max_urls:
#             break
#         crawl(link, max_urls=max_urls)
#
#
# if __name__ == "__main__":
#     url = "https://www.google.com/"
#     max_urls = 1
#
#     crawl(url, max_urls=max_urls)
#
#     print("[+] Total Internal links:", len(internal_urls))
#     print("[+] Total External links:", len(external_urls))
#     print("[+] Total URLs:", len(external_urls) + len(internal_urls))
#
#     domain_name = urlparse(url).netloc
#     # links = get_all_website_links('https://www.google.com/')
#     for each in internal_urls:
#         print(each)

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

    #print(len(ref[url]))
    # s1 = Counter(ref[url])
    #for t_link in ref[url]:
    tarr = []
    for t in ref:
        for k in ref[t]:
            if url == k:
                if t != url:
                    tarr.append(t)
    ref_to = set(tarr)

    for tl in ref_to:
        if pr_urls.get(tl):
            pr_links += pr_urls.get(tl) / internal_urls.count(tl)
        else:
            pr_links += 1 / internal_urls.count(tl)

    if pr_urls.get(url):
        previous_result = pr_urls.get(url)

    pr_link = (1 - d) + d * pr_links
    pr_urls[url] = pr_link

    #print(pr_link)

    if abs(previous_result - pr_urls.get(url)) < 0.00000001:
        return -1

    return 0

links = get_url_on_page('https://www.google.com/')

for link in links:
    get_url_on_page(link)

print(Counter(internal_urls))

#ranks = Counter(internal_urls).items()

ranks = set(internal_urls)

#page_ranks = [item for item, count in Counter(internal_urls).items() if count >= 1]

#def idk(set):
    #for s in set:
       # get_page_rank(s, 0.5)

n = 0
flag = True
while(flag):
    for rank in ranks:
        if get_page_rank(rank, 0.5) == -1:
            flag = False
            break
    n += 1
    if n > 888:
        flag = False

print(n)

result_ranks = {}

for rank in ranks:
    # print('url: ' + rank)
    # print('page rank: ' + str(pr_urls.get(rank)))
    result_ranks[rank] = pr_urls.get(rank)

result = set(result_ranks)

for r in result:
    print('url: ' + r)
    print('page rank: ' + str(result_ranks.get(r)))
#
# for all in ref.get('https://www.google.com.ua/imghp'):
#     if(all == 'https://www.google.com.ua/webhp'):
#         print(all)
