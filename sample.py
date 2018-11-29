import xml.etree.cElementTree as Xml
from bs4 import BeautifulSoup
import requests
root = Xml.Element("root")
finance = Xml.SubElement(root, "finance")
with open("data.csv"
          "", 'r')as f1:
    n1 = f1.read().split("\n")
for i in range(0, 6):
    n2 = n1[i]
str = n2.split("::")
url1 = 'https://finance.yahoo.com/quote/'+str[0]+'/financials?p='+str[0]
resp1 = requests.get(url1)
soup = BeautifulSoup(resp1.content, 'html5lib')
s1 = soup.findAll("tr", class_="Bdbw(1px) Bdbc($c-fuji-grey-c) Bdbs(s) H(36px)")
p1 = soup.findAll("td", class_="Fz(s) H(35px) Va(m)")
p2 = soup.findAll("td", class_="Fz(s) Ta(end) Pstart(10px)")
s2 = soup.findAll("tr", class_="Bdbw(1px) Bdbc($c-fuji-grey-c) Bdbs(s) H(36px)")
p3 = soup.findAll("td", class_="Fz(s) H(35px) Va(m)")
p4 = soup.findAll("td", class_="Fz(s) Ta(end) Pstart(10px)")
'''
p5 = soup.findAll("td", class_="Fz(s) H(35px) Va(m)")
p6 = soup.findAll("td", class_="Fz(s) Ta(end) Pstart(10px)")
p7 = soup.findAll("td", class_="Fw(b) Py(8px) Pt(36px)")
p8 = soup.findAll("td", class_="Fw(b) Ta(end) Py(8px) Pt(36px)")

print(len(p5))
print(len(p6))
print(len(p7))
print(len(p8))

file = 'tick1.txt'
with open(file, "w")as f:
for i, j, m, n, a, b, c, d in zip(range(len(p1)), range(len(p2)), range(len(p3)), range(len(p4)), range(len(p5)), range(len(p6)), range(len(p7)), range(len(p8))):
f.write(p1[i].text + "\n" + p2[j].text + "\n" + p3[m].text + "\n" + p4[n].text + "\n" + p5[a].text + "\n" + p6[b].text + "\n" + p7[c].text + "\n" + p8[d].text + "\n")'''

print(len(s1))
print(len(p1))
print(len(p2))
print(len(s2))
print(len(p3))
print(len(p4))
file = "tick2.txt"
with open(file, "w")as f:
    for i, j, m, n, a, b in zip(range(len(s1)), range(len(p1)), range(len(p2)), range(len(s2)), range(len(p3)), range(len(p4))):
        f.write(s1[i].text + "" + p1[j].text + "" + p2[m].text + "" + s2[n].text + p3[a].text + "" + p4[b].text + "\n")
print("Data entered successfully into file")