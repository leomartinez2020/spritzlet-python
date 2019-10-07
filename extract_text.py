import time
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
    #url = "https://hackernoon.com/functional-programming-what-language-should-you-be-talking-313dd8bc379b"
    #url = "https://www.techrepublic.com/article/how-to-get-a-developer-job-the-best-programming-languages-to-learn/"
    #url = "https://www.zdnet.com/article/linus-torvalds-isnt-worried-about-microsoft-taking-over-linux/"
    url = "https://www.forbes.com/sites/googlecloud/2019/10/02/want-to-become-an-ai-first-company-hire-these-people/#601606705c72"
    text = extract_from_url(url)
    #print(crawl_text(text))
    return crawl_text(text)

def pickle_data():
    data = test1()
    with open('datos', 'wb') as foo:
        pickle.dump(data, foo, pickle.HIGHEST_PROTOCOL)

def extract_pickle():
    with open('datos', 'rb') as foo:
        datos = pickle.load(foo)
    return datos

def read_text():
    with open('datos', 'rb') as foo:
        d = pickle.load(foo)
    length = len(d)
    print(length)
    for elem in d:
        print(elem)
        time.sleep(0.3)
