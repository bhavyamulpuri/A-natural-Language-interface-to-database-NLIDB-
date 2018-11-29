#!C:/Users/Bhavya Mulpuri/AppData/Local/Programs/Python/Python36-32/python.exe
import re
import pymysql
# opening and reading stopwords and config files
filestopwords = open('C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/stopwors.txt', 'r')
fileconfig = open('C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/config.txt', 'r')
dataticker = open('C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/data.csv', 'r')
ticker = dataticker.read()
stopwords = filestopwords.read()
config = fileconfig.read()
n = 0
splitstopwords = stopwords.split("\n")
splitticker = ticker.split("\n")
print(splitticker)
splittick=[]
n4=0
for i in splitticker:
    sp=i.split(" ")
    splittick.insert(n4,sp[0])
print(splittick)
# input a question
question = input('Enter a question to find the answer:').casefold()
# print(question)
query = question.split()
querylist = []
# getting the required word other than stopwords and company name
for q in query:
    if q not in splitstopwords and q.upper() not in splittick :
        querylist.insert(n,q)
        n = n + 1
print(querylist)

splitconfig = re.split(r';',config)
count = 0
configlist=[]
for i in splitconfig:
    configlist.insert(n, i.split("\n"))
    # count = count + 1
attribute = ""
at = ""
o = 0
for i in querylist:
    for j in range(0, len(configlist)):
        for k in range(0, len(configlist[j])):
            if ":" in configlist[j][k]:
                colonspiltlist = configlist[j][k].split(":")
                # print(colonspiltlist)
                if i.lower() in colonspiltlist[0].lower():
                    if attribute == "":
                        attribute = i
                    else:
                        attribute = attribute+","+i
                        print(attribute)
                    o = configlist[j][0]
print(o)
conn = pymysql.connect(host='localhost', user='root', password='123456')
cursor = conn.cursor()
cursor.execute('use pythonproject')
cursor.execute("select company_name," + attribute + " from " + o + " ")
result = cursor.fetchall()
at = attribute.split(",")
n = len(at)
company = []
num1 = 0
for i in splittick:
    if i in question.upper():
        company.insert(num1, i.upper())
        num1 = num1 + 1
for i in result:
    for j in company:
        if j in i:
            for k in range(0, n):
                print(at[k], "of", i[0], "is", i[k+1].strip())
# print(result)
# print(result[1])






