#计算指定年份指定月份的天数

import calendar

yeary = int(input('请输入年份：'))
monthm = int(input('请输入月份：'))
monthRange = calendar.monthrange(yeary, monthm)

print(monthRange)