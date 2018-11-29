import lxml.etree as ET
from bs4 import BeautifulSoup
root = ET.Element("Company")
f = open('data.csv', 'r')
symbol_list = []
for data in f:
    names = data.split(" ")
    symbol_list.append(names[0])
# print(symbol_list)
for i in range(0,6):
    finance = ET.SubElement(root,symbol_list[i])
    soup7 = BeautifulSoup(open('C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/TICKERFOLDERS/'+symbol_list[i]+'/profile.html'),"html.parser")
    soup3 = BeautifulSoup(str(soup7.find_all(class_="D(ib) W(47.727%) Pend(40px)")), "html.parser")
    sectorsoup = BeautifulSoup(str(soup7.find_all(class_="D(ib) Va(t)")), "html.parser")
    Sectorresult = sectorsoup.find_all("strong")
    soup4 = soup3.text
    soup5 = soup3.find_all("a")
    x = ET.SubElement(finance, 'Profile')
    Add = ET.SubElement(x, 'Ticker')
    Add.text = symbol_list[i]
    Address = ET.SubElement(x, 'Address')
    Address.text = soup4
    number = ET.SubElement(x, 'Phone_number')
    number.text = soup5[0].text
    website = ET.SubElement(x, 'Webiste')
    website.text = soup5[1].text
    sector = ET.SubElement(x, 'Sector')
    sector.text = Sectorresult[0].text
    industry = ET.SubElement(x, 'Industry')
    industry.text = Sectorresult[1].text
    time = ET.SubElement(x, 'Full_Time')
    time.text = Sectorresult[2].text
    tree = ET.ElementTree(root)
    tree.write("financials.xml")
    print("Profile xml has been created successfully")
    soup = BeautifulSoup(open('C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/TICKERFOLDERS/'+symbol_list[i]+'/finance.html'),"html.parser")
    x=ET.SubElement(finance,'Finance')
    rows = soup.find_all('tr')
    l=len(rows)
    Add = ET.SubElement(x, 'Ticker')
    Add.text = symbol_list[i]
    for tr in range(0,l):
        tdata = rows[tr].find_all('td')
        st = tdata[0].span.text
        s = str(st).lstrip()
        if (tr == 1):
            val = tdata[1].span.text
            Total_Revenue = ET.SubElement(x, 'Total_Revenue')
            Total_Revenue.text = val
        elif (tr == 2):
            val = tdata[1].span.text
            Cost_of_Revenue = ET.SubElement(x, 'Cost_of_Revenue')
            Cost_of_Revenue.text = val
        elif (tr == 15):
            val = tdata[1].span.text
            Income_before_tax = ET.SubElement(x, 'Income_before_tax')
            Income_before_tax.text = val
        elif (tr == 25):
            val = tdata[1].span.text
            Net_Income = ET.SubElement(x, 'Net_Income')
            Net_Income.text = val
    tree = ET.ElementTree(root)
    tree.write("financials.xml")
    print(" Finance xml has been created successfully")
    soup1 = BeautifulSoup(open('C:/Users/Bhavya Mulpuri/PycharmProjects/PYTHONPROJECT/TICKERFOLDERS/'+symbol_list[i]+'/statistics.html'),"html.parser")
    d = soup1.find_all(class_='table-qsp-stats Mt(10px)')
    soup2 = BeautifulSoup(str(d), 'html.parser')
    names = soup2.find_all('span')
    d1 = soup1.find_all(class_="Fz(s) Fw(500) Ta(end)")
    soup2 = BeautifulSoup(str(d1), 'html.parser')
    number = soup2.find_all()
    l = len(number)
    x=ET.SubElement(finance,'Statistics')
    j = 0
    Add = ET.SubElement(x, 'Ticker')
    Add.text = symbol_list[i]
    for i in number:
        if j == 0:
            Marketcap = ET.SubElement(x, 'Market_Cap')
            Marketcap.text = i.text
        if j == 1:
            enter = ET.SubElement(x, 'Enterprise_Value')
            enter.text = i.text
        if j == 15:
            assets = ET.SubElement(x, 'Return_on_Assets')
            assets.text =i.text
        if j == 25:
            cash = ET.SubElement(x, 'Total_cash')
            cash.text =i.text
        if j == 31:
            flow = ET.SubElement(x, 'Operating_cash_flow')
            flow.text = i.text
        if j == 32:
            cash_flow= ET.SubElement(x, 'Levered_free_cash_flow')
            cash_flow.text =i.text
        if j == 27:
            debt = ET.SubElement(x, 'Total_debt')
            debt.text = i.text
        if j == 29:
            ratio = ET.SubElement(x, 'Current_ratio')
            ratio.text =i.text
        if j == 20:
            pf = ET.SubElement(x, 'Gross_profit')
            pf.text =i.text
        if j == 13:
            mg = ET.SubElement(x, 'Profit_margin')
            mg.text =i.text
        j = j + 1
        tree = ET.ElementTree(root)
        tree.write("financials.xml")
print("Statistics xml has been created successfully")

