# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:35:14 2018

@author: GANGZ
"""

#第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

from a0001 import get_tickets
import mysql.connector

try:
    conn = mysql.connector.connect(
            user='root', 
            password='123456', 
            database='test', 
            use_unicode=True)
    
    cursor = conn.cursor()
    
#   cursor.execute('create table tickets(id int, ticket_str varchar(50), used boolean default false)'))
    
    tickets = get_tickets(200)

#   method 1 : use for loop to insert 200 times
#    for id, ticket in enumerate(tickets):
#        cursor.execute('insert into tickets(id, ticket_str, used) values (%s, %s, %s)', (id, ticket,0))

#   method 2 : use cursor.executemany() to insert 200 rows one time
    stmt = 'insert into tickets(id, ticket_str, used) values (%s, %s, %s)'
    data = [(i+200, ticket, 0) for i, ticket in enumerate(tickets)]
    
    cursor.executemany(stmt, data)
    
    print(cursor.rowcount)
    conn.commit()
    
except Exception as e:
    print(e)
    conn.rollback()
    
finally:
    cursor.close()
