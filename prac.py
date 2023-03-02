import pandas as pd
import numpy as np

# data = pd.read_csv('C:\\Users\\1003647\\Desktop\\FLASK_API\\data.csv')
# print(data)

file=open('C:\\Users\\1003647\\Desktop\\FLASK_API\\data.csv')

lines=file.readlines()
# print(lines)
processedlist=[]
for i,line in enumerate(lines):
    try:
        line=line.split(',')
        last=line[3].split(';')[0]
        last=last.strip()
        processedlist.append([line[0],line[1],line[2],last])
    except:
        print('error in line',i)
# data=pd.DataFrame(processedlist)
# print(data)

# for i,line in enumerate(lines):
#     try:
#         line=line.split(',')
#         last=line[3].split(';')[0]
#         last=last.strip()
#         if last=='':
#             break
#         # print(i,line)
#         temp=[line[0],line[1],line[2],last]
#         processedlist.append(temp)
#     except:
#         print("error in line ",i)
print(processedlist)

# data=pd.DataFrame(processedlist)
# print(data)