'''从CSV文件中读取数据并绘制带区域着色的曲线图'''

import matplotlib.pyplot as plt
from datetime import datetime  #日期格式模块
import csv
import os

path = os.getcwd()
file = path + '\death_valley_2014.csv'

with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, max_temp, min_temp = [], [], []
    for row in reader:
        '''处理数据缺失现象'''
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')#按指定格式将字符串转换成日期
            high = int(row[1])
            lower = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            max_temp.append(high)
            min_temp.append(lower)

fig = plt.figure(figsize=(10, 6), dpi=120)
plt.plot(dates, max_temp, c='red', alpha=0.5)#绘制最高气温曲线
plt.plot(dates,min_temp, c='blue', alpha=0.5)#绘制最低气温曲线
plt.fill_between(dates, max_temp, min_temp, alpha=0.1)#在两条曲线间着色

plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA')
plt.xlabel('', fontsize= 16)
plt.ylabel('Temperatures(F)', fontsize= 16)
plt.ylim(20, 110)#设置y轴范围
fig.autofmt_xdate()#设置斜的日期显示方式
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig('Death_Valley_Temperature.png', bbox_inches='tight')
