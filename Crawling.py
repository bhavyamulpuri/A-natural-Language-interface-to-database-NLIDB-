from bs4 import BeautifulSoup
import requests
import os

# getting URL
URL = 'https://finance.yahoo.com/trending-tickers'
source = requests.get(URL)
soup = BeautifulSoup(source.content, 'html5lib')

# getting class ids and storing the data in a var
a = soup.findAll("td", class_="data-col0 Ta(start) Pstart(6px) Pend(15px)")
b = soup.findAll("td", class_="data-col1 Ta(start) Pstart(10px) Miw(180px)")

# Creating csv fie and storing the tickers along with the name of companies
with open("data.csv", "w")as f:
    # zip is used to append a and b
    for i, j in zip(range(len(a)), range(len(b))):
        # print(a[i].text)
        f.write(a[i].text+" "+b[j].text + "\n")

folders = ['key-statistics', 'profile', 'financials']

# opening the file to get the data to append to the folders
file = open('data.csv', 'r')
data = file.read()
s = data.split("\n")
print("1.")
print(s)
for index in range(0, 6):
    company = s[index]
    title = company.split(" ")
    # print("2.")
    print(title[0])
     # path = 'C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/TICKERFOLDERS/' + title[0]

    for i in range(0, 6):
        line = data[i]
        print(line)
        print("+++++++++++++++++++")

        str = line.split(" ")
        print(str)
    print(title[0], title[1])
    stats = 'https://finance.yahoo.com/quote/' + title[0] + '/key-statistics?p=' + title[0]
    req1 = requests.get(stats)

    profile = 'https://finance.yahoo.com/quote/' + title[0] + '/profile?p=' + title[0]
    print(profile)

    req2 = requests.get(profile)

    finance = 'https://finance.yahoo.com/quote/' + title[0] + '/financials?p=' + title[0]
    print(finance)
    req3 = requests.get(finance)

    soup1 = BeautifulSoup(req1.content, 'html5lib')

    soup2 = BeautifulSoup(req2.content, 'html5lib')

    soup3 = BeautifulSoup(req3.content, 'html5lib')

    path1 = 'C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/TICKERFOLDERS/' + title[0] + '/finance.html'
    f1 = open(path1, 'w')
    f1.write(soup3.prettify())

    path2 = 'C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/TICKERFOLDERS/' + title[0] + '/profile.html'
    f2 = open(path2, 'w')
    f2.write(soup2.prettify())

    path3 = 'C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/TICKERFOLDERS/' + title[0] + '/statistics.html'
    f3 = open(path3, 'w')
    f3.write(soup1.prettify())
    print("entered sucessfully")

    # # checking whether the directory is present or no
    # if not os.path.exists(path):
    #     os.makedirs(path)

