import time
import re
import random
import pickle
import requests
from bs4 import BeautifulSoup

def extract_from_url(url):
    res = requests.get(url)
    return res.text

def crawl_text(text):
    sopa = BeautifulSoup(text)
    p_text = sopa.find_all('p')
    arr_texto = [elem.text for elem in p_text]
    readme = ' '.join(arr_texto)
    leeme = readme.split()
    return leeme

def test1():
    url1 = "https://hackernoon.com/functional-programming-what-language-should-you-be-talking-313dd8bc379b"
    url2 = "https://www.techrepublic.com/article/how-to-get-a-developer-job-the-best-programming-languages-to-learn/"
    url3 = "https://www.zdnet.com/article/linus-torvalds-isnt-worried-about-microsoft-taking-over-linux/"
    url4 = "https://www.forbes.com/sites/googlecloud/2019/10/02/want-to-become-an-ai-first-company-hire-these-people/#601606705c72"
    url5 = "https://www.geekwire.com/2019/amazon-launches-aws-iq-marketplace-third-party-cloud-experts-demand-projects/"
    text = extract_from_url(url5)
    #print(crawl_text(text))
    return crawl_text(text)

url1 = "https://hackernoon.com/functional-programming-what-language-should-you-be-talking-313dd8bc379b"
url2 = "https://www.techrepublic.com/article/how-to-get-a-developer-job-the-best-programming-languages-to-learn/"
url3 = "https://www.zdnet.com/article/linus-torvalds-isnt-worried-about-microsoft-taking-over-linux/"
url4 = "https://www.forbes.com/sites/googlecloud/2019/10/02/want-to-become-an-ai-first-company-hire-these-people/#601606705c72"
url5 = "https://www.geekwire.com/2019/amazon-launches-aws-iq-marketplace-third-party-cloud-experts-demand-projects/"
url6 = "https://www.businessinsider.com/10-key-skills-to-succeed-as-a-cloud-architect-2019-9"

url_list = [url1, url2, url3, url4, url5, url6]

def test2(url):
    text = extract_from_url(url)
    return crawl_text(text)

def pickle_text(textfile):
    with open(textfile, 'r') as bar:
        content = bar.read()
    lista = content.split()
    filename = random.choice(lista) + random.choice(lista)
    with open(filename, 'wb') as foo:
        pickle.dump(lista, foo, pickle.HIGHEST_PROTOCOL)
    print(f"file {filename} created...")

def pickle_data(url):
    name = re.search("www\.(\w+)\.com", url)
    filename = name.group()
    data = test2(url)
    with open(filename, 'wb') as foo:
        pickle.dump(data, foo, pickle.HIGHEST_PROTOCOL)
    print(f"file {filename} created...")

def extract_pickle(filename):
    with open(filename, 'rb') as foo:
        datos = pickle.load(foo)
    return datos

def read_text(filename):
    with open(filename, 'rb') as foo:
        d = pickle.load(foo)
    length = len(d)
    print(length)
    for elem in d:
        print(elem)
        time.sleep(0.3)
