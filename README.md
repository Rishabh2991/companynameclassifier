# companynameclassifier
1. scrapy_scraper.py: A command line utility to extract website name for a particular organization name and scrap the website 
for text data. This python uses a BeautifulSoup method along with python's scrapy framework to perform web crawling on  google's keyword search results (https://www.google.co.in/search?q=). It will look for the first href tag in the output to get the probable website name of the company and perform text keywords search on content present on that website



2. classfier.py : A classifier which can take input from module 1 and perform classification with Naive Bayes algorithm. This method reads a set of mocked up data present in company_data.txt file , where it perfoms feature vectorization and then breaks it into train test sets and create a naive bayes classifier.

3. companydata_test.txt : A sample of company data scraped from web.
