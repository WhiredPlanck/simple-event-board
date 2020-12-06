#!/usr/bin/env python
#-*- coding:utf-8 -*-

import datetime
from calendar import isleap

month = 6
firstday = 7
today = datetime.date.today()
def IsThisYear(): #判断是否已过今年时间
    if today.month < month: #本月小于 6 月，那么今年没过
        return True
    elif today.month == month: #等于 6 月，判断是否小于第一天日期
        if today.day > firstday: #大于，那么今年已过
            return False
        else:                    #否则小于等于，今年没过或正好到了
            return True
    else:                      #大于 6 月，今年已过
        return False

def DaysLeft(): #计算距离下一次还有多少天
    nlymd = [31,28,31,30,31,30,31,31,30,31,30,31]
    total = 0
    if IsThisYear(): #如果是今年 ...
        for i in nlymd[(today.month - 1):5]:
            total += i
        if isleap(today.year): #判断今年是否为闰年
            '''
            for i in nlymd[(today.month - 1):5]:
                total += i + 1
            '''
            daysleft = total + firstday - 1 - today.day + 1
        else:
            '''
            for i in nlymd[(today.month - 1):5]:
                total += i
            '''
            daysleft = total + firstday - 1 - today.day 
    else: #如果是明年 ...
        for i in nlymd[0:5]:
                total += i
        for j in nlymd[(today.month - 1)::]:
                total += j
        if isleap(today.year + 1): #判断明年是否为闰年
            '''
            for i in nlymd[0:5]:
                total += i + 1
            for j in nlymd[(today.month - 1)::]:
                total += j
            '''
            daysleft = total - 1 - today.day + firstday + 1 
        else:
            '''
            for i in nlymd[0:5]:
                total += i
            for j in nlymd[(today.month - 1)::]:
                total += j
            '''
            daysleft = total - 1 - today.day + firstday
    return daysleft