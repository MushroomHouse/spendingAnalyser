# -*- coding: UTF-8 -*- 
import os
import pprint
import csv
import datetime
import sys
import matplotlib.pyplot as plt

def parse_csv(datafile):
    costPerYear = {}
    with open(datafile, "rb") as sd:
        r = csv.DictReader(sd)   #为每行创建一个字典，同时将字段名称与表头对应
        for line in r:
            #print line['Date'], "spend:", line['Amount']
            dateStr = line['Date']
            date = datetime.datetime.strptime(dateStr, "%Y-%m-%d  %H:%M:%S")
            amount = float(line['Amount'])
            if amount < 0:  # We are only parsing costs
                amount = int(amount * (-1))
                if date.year not in costPerYear:
                    costPerYear[date.year] = amount
                else:
                    costPerYear[date.year] += amount
    return costPerYear

def autolabel(rects):
 for rect in rects:
  height = rect.get_height()
  plt.text(rect.get_x()+rect.get_width()/2.-0.3, 1.03*height, '%s' % float(height))

def drawPic(dataDic):
    name_list = []
    num_list = []
    for key in sorted(dataDic.iterkeys()):
        name_list.append(key)
        num_list.append(dataDic[key])

    a = plt.bar(range(len(num_list)), num_list, color = 'rgb', tick_label = name_list)

    plt.xlabel("Cost")  #设置X轴Y轴名称  
    plt.ylabel("Year")  
    plt.title("Expenses in Vancouver")
    #使用text显示数值  
    autolabel(a)

    plt.ylim(0, 100000)
    plt.show()

if __name__ == '__main__':
    datafile = os.path.join("", str(sys.argv[1]))
    d = parse_csv(datafile)
    pprint.pprint(d)
    drawPic(d)


