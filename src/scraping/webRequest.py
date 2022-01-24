import os #for navigating directories
import requests #for requesting urls
import csv #for handling csv files
import pandas as pd #for data handling
from datetime import datetime #for working with dates and time
from bs4 import BeautifulSoup as soup #for parsing web pages
print("succesfully imported modules")
#define the URL where the web page can be accessed
url="https://www.worldometers.info/coronavirus/"
#request the web page from the url
response=requests.get(url,allow_redirects=True)#request the url
response.status_code #check if request id successful 
#print(response.text[:1000])
#Extract the contents of the web page from the response
soup_response=soup(response.text,"html.parser")# Parse the text as a beautiful soup object
soup_sample= soup(response.text[:10000],"html.parser")#Parse a sample of the text
#print(str(soup_sample))
sections=soup_response.find_all("div",id="maincounter-wrap")
#print(str(sections)) note: len(sections)=3
cases=sections[0].find("span").text.replace(" ","").replace(",","")#text replace to clean spaces and commas
deaths=sections[1].find("span").text.replace(",","")
recov=sections[2].find("span").text.replace(",","")
print("Number of cases:{};deaths:{};recoveries:{}".format(cases,deaths,recov))

