# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:03:17 2018

@author: GANGZ
"""

#第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

from a0001 import get_tickets
from redis import StrictRedis

# 连接
redis = StrictRedis(host='localhost', port=6379, db=0)

# 获取tickets
tickets = get_tickets(200)

# 删除并插入数据
redis.delete('tickets')
redis.rpush('tickets', *tickets)
print('length of tickets is :', redis.llen('tickets'))

# 查询并检查结果是否一致
tickets_from_redis = [x.decode() for x in redis.lrange('tickets', 0, 200)]

print(tickets == tickets_from_redis)
print(tickets)
print(tickets_from_redis)
