# -*- coding:utf-8 -*-
import re

with open('1.srt', "r") as f:
    data= f.readlines()
    #print (data)
    hour_list=[]
    minute_list=[]
    second_list =[]
    for line in data:
        result=re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2}',line)
        if result != []:
            #print(result)
            for item in result:
                hour=item.split(':')[0]
                minute=item.split(':')[1]
                second=item.split(':')[2]
                hour_list.append(hour);minute_list.append(minute);second_list.append(second)
print(minute_list[60],second_list[60])
for sec in second_list:
    index_s = second_list.index(sec)
    if sec != '59':
        if sec == '00' or sec == '01'or sec == '02'or sec == '03' or sec=='04' or sec == '05' or sec=='06' or sec=='07' or sec=='08':
            sec_value = eval(sec[1])+1
            second_list[index_s] = '0'+str(sec_value)
        elif sec == '09':
            sec = '10'
        else:
            sec = str(eval(sec)+1)
            second_list[index_s] = sec
    else:
        sec='00'
        if minute_list[index_s] == '00' or minute_list[index_s] == '01'or minute_list[index_s] == '02'or minute_list[index_s] == '03' or minute_list[index_s]=='04' or minute_list[index_s] == '05' or minute_list[index_s]=='06' or minute_list[index_s]=='07' or minute_list[index_s] =='08':
            min_value = eval((minute_list[index_s])[1])+1
            minute_list[index_s] = '0'+str(min_value)
        elif minute_list[index_s] =='09':
            minute_list[index_s] = '10'
        else:
            minute_list[index_s]= str(eval(minute_list[index_s])+1)
        
#second_list[61] = '0'+str(eval((second_list[61])[1])+1)


print(minute_list[60],second_list[60])
        


