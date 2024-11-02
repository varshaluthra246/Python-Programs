import math
import statistics as st
radius = 10000000
area = math.pi * radius * radius
print("area",area)
modee=st.mode([56,36,85,247,62,9,69,68,65,69,76,87,69,876,69,686,69,-654])
med=st.median([45,74,96,32,655,11,1,9,74,96,69,69,96,72,678,72,678,74,45,69,69,79,678])
mea=st.mean([2,3,4,5,6,7,8,9,70,54,23,654,69,834])
print('mode=',modee,'median=',med,'mean=',mea)
stdeviation=st.stdev([67,76,75,84,3,4,9,8,7,6,5,4,6,1,87,69,143])
print(stdeviation)

import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
