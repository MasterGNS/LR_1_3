from bs4 import BeautifulSoup
import requests
import re

def pars():
    url= "https://www.omgtu.ru/university/about-the-university/persons/"
    file = open("bebra.txt","w")
    page= requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    Prep = []
    SortPrep = []
    prep = soup.findAll("div", style ="padding: 5px; font-size: 120%;")
    for n in prep:
        if n.find(string = re.compile(" Н")) is not None:
            SortPrep.append(n.text)
    for sn in SortPrep:
        words = sn.split()
        if words[0][0] == "Н":
            file.write(sn.strip()+ "\n")