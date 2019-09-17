import scrapy
import os
import re
import sys
from scrapy.selector import Selector 
from scrapy.crawler import CrawlerProcess
import requests
from bs4 import BeautifulSoup

class Myspider(scrapy.Spider):
    name = "search"
    print(str(sys.argv[1]))
    search = str(sys.argv[1]).replace(' ','+').lower()
    url = 'https://www.google.co.in/search?q=' + search
    print(url)

    start_urls = [url]
    
    def __init__(self):
        pass
    
    def parse(self,response):
        text_from_html = []
        html = response.xpath('//div[@class="g"]')[0].extract()
        print("++++++++")
        #print(html)
        print("++++++++")
        resultset = Selector(text=html).xpath('//h3[@class="r"]//a[@href]')[0].xpath("@href").extract()
        print("++++++++")
        result = str(resultset).split('/url?q=')[1].split('&')[0]
        print(result)
        page = requests.get(result)
        html_cont = page.content
        soup = BeautifulSoup(html_cont,'html.parser')
        for script in soup(["script", "style"]):
            script.decompose() 
        texts = soup.get_text()
        print(type(texts))
        lines = (line.strip() for line in texts.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        texts = '\n'.join(chunk for chunk in chunks if chunk)
        print(texts)
        #text_from_html.append[texts]


process = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(Myspider)
process.start()
    
