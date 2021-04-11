# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 19:32:52 2021

@author: rkandepi
"""
#importing packages

import pandas as pd
import numpy as np
#Reading the inputfile

InputFilePath="/Users/rkandepi/Downloads/Python_Assignment.xlsx"

Maths=pd.read_excel(InputFilePath,"Maths")
Physics=pd.read_excel(InputFilePath,"Physics")
Hindi=pd.read_excel(InputFilePath,"Hindi")
Economics=pd.read_excel(InputFilePath,"Economics")
Music=pd.read_excel(InputFilePath,"Music")

# Getting All Unique Students Roll No and Classes

All_Students=pd.concat([Maths[['Roll No','Class']],Physics[['Roll No','Class']],Hindi[['Roll No','Class']],Economics[['Roll No','Class']],Music[['Roll No','Class']]]).drop_duplicates(['Roll No','Class']).reset_index(drop=True)

#Caluclating Total Avg Marks per Subject

Maths['Maths']=(Maths['Theory Marks']+Maths['Numerical Marks']+Maths['Practical Marks'])*100/300
Physics['Physics']=(Physics['Theory Marks']+Physics['Numerical Marks']+Physics['Practical Marks'])*100/300
Hindi['Hindi']=(Hindi['Marks'])*100/100
Economics['Economics']=(Economics['Theory Marks']+Economics['Numerical Marks'])*100/200
Music['Music']=(Music['Theory Marks']+Music['Practical Marks'])*100/200


#####################   Question 1   ###########################################

All_Students=pd.merge(All_Students,Maths[['Roll No','Class','Maths']],how='left' ,left_on=['Roll No','Class'],right_on=['Roll No','Class'])
All_Students=pd.merge(All_Students,Physics[['Roll No','Class','Physics']],how='left' ,left_on=['Roll No','Class'],right_on=['Roll No','Class'])
All_Students=pd.merge(All_Students,Hindi[['Roll No','Class','Hindi']],how='left' ,left_on=['Roll No','Class'],right_on=['Roll No','Class'])
All_Students=pd.merge(All_Students,Economics[['Roll No','Class','Economics']],how='left' ,left_on=['Roll No','Class'],right_on=['Roll No','Class'])
All_Students=pd.merge(All_Students,Music[['Roll No','Class','Music']],how='left' ,left_on=['Roll No','Class'],right_on=['Roll No','Class'])

All_Students1=All_Students.fillna('NA')
All_Students1.sort_values(['Class','Roll No']).to_csv("Output.csv")

##################### Question 2 ###############################################

               ####### 2.1########
print("{0} students in total are enrolled with the tuition provider" .format(len(All_Students)))


               ####### 2.2##########

print("{0}  students have taken all the five subjects".format(len(All_Students.dropna())))


               ####### 2.3##########  

max1=All_Students[['Class','Roll No']].groupby(["Class"]).count()
max1=max1.reset_index()

x=max1['Class'].tolist()
y=max1['Roll No'].tolist()
new_dict = {}
for i in range(min(len(x),len(y))) :
    new_dict[x[i]] =y[i] 
  
maxValue = max(new_dict.values())
max_key1=[k for k, v in new_dict.items() if v == maxValue]
print("Classes {0}  has the most number of students".format(max_key1))



               ######## 2.4#########


All_Students['avg'] = All_Students[['Maths', 'Physics','Hindi','Economics','Music']].mean(axis=1)
max2=pd.DataFrame(All_Students[['Class','avg']].groupby(["Class"]).max())
max2=max2.reset_index()
x1=max2['Class'].tolist()
y1=max2['avg'].tolist()
new_dict1 = {}
for i in range(min(len(x1),len(y1))) :
    new_dict1[x1[i]] =y1[i] 
maxValue1 = max(new_dict1.values())
max_key2=[k for k, v in new_dict1.items() if v == maxValue1]
print("Classes {0} has the highest average percentage of marks across all subjects".format(max_key2))


             ########## 2.5########

dict={}
list=['Maths','Physics','Hindi','Economics','Music']
for i in list:
      x =All_Students[i].max()
      dict[i]=x
      
maxValue2 = max(new_dict1.values())
max_key3=[k for k, v in dict.items() if v == maxValue2]
print("Subject {0} has the highest average percentage of marks across all classes".format(max_key3))




