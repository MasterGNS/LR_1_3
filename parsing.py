from bs4 import BeautifulSoup
import requests
import re

def filez(sn,file):
    file.write(sn.strip() + "\n")

def pars():
    url= "https://www.omgtu.ru/university/about-the-university/persons/"
    page= requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    Prep = []
    SortPrep = []
    prep = soup.findAll("div", style ="padding: 5px; font-size: 120%;")
    for n in prep:
        if n.find(string = re.compile(" Н")) is not None:
            SortPrep.append(n.text)
    file = open("bebra.txt", "w")
    for sn in SortPrep:
        words = sn.split()
        if words[0][0] == "Н":
            filez(sn,file)
    file.close()
