# -*- coding: utf-8 -*-
# @Author: gang zhang
# @Date:   2018-10-10 15:47:27
# @Last Modified by:   gang zhang
# @Last Modified time: 2018-10-10 16:33:48
#第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码
#（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random

def get_tickets(num):
    
    
    #a = 97
    #a_cap = 65
    
    #l = [str(x) for x  in list(range(0,10))]
    #l.extend([chr(a) for a in range(a,a+26)])
    #l.extend([chr(a) for a in range(a_cap,a_cap+26)])
    
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
        'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
        'U', 'V', 'W', 'X', 'Y', 'Z']
            
    
    tickets = []
    for i in range(num):
        ticket = '-'.join([''.join(random.sample(l,4)) for x in range(5) ])
        tickets.append(ticket)
    
    return tickets[:]

if __name__ == '__main__':
    
    num = 5
    print(get_tickets(num))