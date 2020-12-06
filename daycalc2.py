 #!/usr/bin/env python
#-*- coding:utf-8 -*-

import datetime

e_month = 6
e_day = 7
today = datetime.date.today()

def is_this_year(): #判断是否已过今年时间
    if today.month < e_month: #本月小于事件发生月份，那么今年没过
        return True
    elif today.month == e_month: #等于事件发生月份，判断是否小于发生日期
        if today.day > e_day: #大于，那么今年已过
            return False
        else:                    #否则小于等于，今年没过或正好到了
            return True
    else:                      #大于事件所在月份，今年已过
        return False
    
def show_year():
    if is_this_year():
        return today.year
    else:
        return today.year + 1

def days_left(): #计算距离下一次还有多少天
    if is_this_year():
        days = (datetime.date(today.year, e_month, e_day) - today)
    else:
        days = (datetime.date(today.year + 1, e_month, e_day) - today)

    return days.days
