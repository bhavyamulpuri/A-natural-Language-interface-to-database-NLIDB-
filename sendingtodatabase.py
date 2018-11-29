import pymysql
import lxml.etree as ET

connections = pymysql.connect(host='localhost', user='root', password='123456')
cursor = connections.cursor()
cursor.execute('use pythonproject')

try:
    table = 'drop table finance'
    cursor.execute(table)
except Exception as e:
    pass
try:
    table = 'drop table profiles'
    cursor.execute(table)
except Exception as e:
    pass
try:
    table = 'drop table statistics'
    cursor.execute(table)
except Exception as e:
    pass
try:
    table = 'create table finance(company_name varchar(200), Net_income varchar(100),totalrevenue varchar(100),costofRevenue varchar(100),income_before_tax varchar(100))'
    cursor.execute(table)
except Exception as e:
    pass
try:
    table = 'create table profiles(company_name varchar(200),address varchar(500),phonenumber varchar(100),website varchar(200),sector varchar(200),industry varchar(200),full_time varchar(100))'
    cursor.execute(table)
except Exception as e:
    pass
try:
    table = 'create table statistics(company_name varchar(200),marketcap varchar(200),enterprisevalue varchar(200),return_on_assets varchar(200),total_cash varchar(200),open_cash_flow varchar(200),levered_free_cash_flow varchar(200),Total_debt varchar(200),current_ratio varchar(200),gross_profit varchar(200),profit_margin varchar(200))'
    cursor.execute(table)
except Exception as e:
    pass

file=ET.parse('financials.xml')
tree=file.getroot()

list = []
for i in tree:

    for j in i:

        for k in j:
            list.append(k.text)
        length = len(list)
        if length==11:
            row="insert into statistics values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10])
            cursor.execute(row)
            connections.commit()
            list.clear()
        elif length==7:
            row = "insert into profiles values('%s','%s','%s','%s','%s','%s','%s')" % (list[0], list[1], list[2], list[3], list[4], list[5], list[6])
            cursor.execute(row)
            connections.commit()
            list.clear()
        elif length==5:
            row = "insert into finance values('%s','%s','%s','%s','%s')" % (list[0], list[1], list[2], list[3], list[4])
            cursor.execute(row)
            connections.commit()
            list.clear()
