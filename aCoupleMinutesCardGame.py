# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:38:24 2021

@author: owner
"""
print(f'【關係同步卡牌的號碼統計】\n')

#五種主題的卡牌號碼
friend_date = [24, 26, 75, 27, 3, 90, 4, 20, 35, 94]
first_date = [3, 18, 35, 13, 26, 41, 5, 21, 95, 23]
happy_trip = [7, 28, 11, 76, 19, 6, 17, 8, 30, 14]
cozy_trip = [15, 31, 24, 16, 25, 44, 10, 43, 1, 33]
heavy_date = [32, 42, 36, 60, 46, 71, 56, 85, 93, 34]

#將五種主題的卡牌號碼整理成已有的卡牌號碼集合
had_numbers = friend_date + first_date + happy_trip + cozy_trip + heavy_date
#印出已有卡牌的數量
print(f'在主題中已有卡牌的數量有{len(had_numbers)}張')

#排序並印出已有的卡牌號碼
had_numbers.sort()
print(f'已有的卡牌號碼為：\n{had_numbers}')
print( f'{"我是分隔線":=^60}')

#剩餘卡牌集合，其中又可分為三級
rest = []
rest1 = []
rest2 = []
rest3 = []

#比對並印出level1的剩餘卡牌號碼有哪些及數量
for i in range(1, 34):
      
    for n in range(len(had_numbers)):
        
        if had_numbers[n] == i:
            break
               
        elif had_numbers[n] < i:
            pass
        
        else:
            rest1.append(i)
            break
nextStart = n
print(f'level 1 的剩餘卡牌有{len(rest1)}張')
print(f'level 1 的剩餘卡牌號碼為：{rest1}')
print( f'{"-":-^60}')

#比對並印出level2的剩餘卡牌號碼有哪些及數量
for i in range(34, 67):
      
    for n in range(nextStart, len(had_numbers)):
        
        if had_numbers[n] == i:
            break
               
        elif had_numbers[n] < i:
            pass
        
        else:
            rest2.append(i)
            break
nextStart = n
print(f'level 2 的剩餘卡牌有{len(rest2)}張')
print(f'level 2 的剩餘卡牌號碼為:{rest2}')
print( f'{"-":-^60}')
        
#比對並印出level3的剩餘卡牌號碼有哪些及數量
for i in range(67, 100):
      
    for n in range(nextStart, len(had_numbers)):
        
        if had_numbers[n] == i:
            break
               
        elif (had_numbers[n] < i) and (n != (len(had_numbers)-1)) :
            pass
        
        else:
            rest3.append(i)
            break
print(f'level 3 的剩餘卡牌有{len(rest3)}張')
print(f'level 3 的剩餘卡牌號碼為：{rest3}')
print( f'{"-":-^60}')
     
#印出所有剩餘的卡牌號碼極其數量
rest  = rest1 + rest2 + rest3
print(f'所有剩餘的卡牌有{len(rest)}張')
print(f'所有剩餘的卡牌號碼為：\n{rest}')
