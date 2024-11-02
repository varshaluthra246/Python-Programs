#Creation of an empty DataFrame
import pandas as pd
import numpy as np

df1 = pd.DataFrame()
print(df1)
print()

#Creation of DataFrame from NumPy ndarrays
array1 = np.array([10,20,30])
array2 = np.array([100,200,300])
array3 = np.array([-10,-20,-30, -40])
df2 = pd.DataFrame(array1)
print(df2)
print()

df6 = pd.DataFrame([array1, array2, array3], columns=[ 'A', 'B', 'C', 'D'])
print(df6)
print()

#Creation of DataFrame from List of Dictionaries
listDict = [{'a':10, 'b':20}, {'a':5, 'b':10, 'c':20}]
df7 = pd.DataFrame(listDict)
print(df7)
print()

#Creation of DataFrame from Dictionary of Lists
dictForest = {'State': ['Assam', 'Delhi', 'Kerala'],
              'GArea': [78438, 1483, 38852] ,
              'VDF' : [2797, 6.72,1663]}
df8= pd.DataFrame(dictForest)
print(df8)
print()

# Creation of DataFrame from Series
seriesA = pd.Series([1,2,3,4,5],
 index = ['a', 'b', 'c', 'd', 'e'])
seriesB = pd.Series ([1000,2000,-1000,-5000,1000],
 index = ['a', 'b', 'c', 'd', 'e'])
seriesC = pd.Series([10,20,-10,-50,100],
 index = ['z', 'y', 'a', 'c', 'e'])

df9 = pd.DataFrame(seriesA)
print(df9)
print()

df10 = pd.DataFrame([seriesA, seriesB])
print(df10)
print()

df11 = pd.DataFrame([seriesA, seriesC])
print(df11)
print()

#Creation of DataFrame from Dictionary of Series
ResultSheet={'Arnab': pd.Series([90, 91, 97],
             index=['Maths','Science','Hindi']),
             'Ramit': pd.Series([92, 81, 96],
             index=['Maths','Science','Hindi']),
             'Samridhi': pd.Series([89, 91, 88],
             index=['Maths','Science','Hindi']),
             'Riya': pd.Series([81, 71, 67],
             index=['Maths','Science','Hindi']),
             'Mallika': pd.Series([94, 95, 99],
             index=['Maths','Science','Hindi'])}
ResultDF = pd.DataFrame(ResultSheet)
print(ResultDF)
print()

dictForUnion = { 'Series1' : pd.Series([1,2,3,4,5],
                  index = ['a', 'b', 'c', 'd', 'e']) ,
                 'Series2' : pd.Series([10,20,-10,-50,100],
                  index = ['z', 'y', 'a', 'c', 'e']),
                 'Series3' : pd.Series([10,20,-10,-50,100],
                  index = ['z', 'y', 'a', 'c', 'e']) }

df12 = pd.DataFrame(dictForUnion) 
print(df12)
print()


#Operations on rows and columns in DataFrames
#Adding a New Column to a DataFrame
ResultDF['Preeti']=[89,78,76]
print(ResultDF)
print()

ResultDF['Arnab']=90
print(ResultDF)
print()


# Adding a New Row to a DataFrame
ResultDF.loc['English'] = [85, 86, 83, 80, 90, 89]
print(ResultDF)
print()


ResultDF.loc['English'] = [95, 86, 95, 80, 95,99]
print(ResultDF)
print()

ResultDF.loc['Maths']=0
print(ResultDF)
print()


ResultDF[: ] = 0
print(ResultDF)
print()


#Deleting Rows or Columns from a DataFrame
ResultDF1 = ResultDF.drop('Science', axis=0)         #row
print(ResultDF1)
print()

ResultDF2 = ResultDF.drop(['Samridhi','Ramit','Riya'], axis=1)
print(ResultDF2)
print()


#Renaming Row Labels of a DataFrame
ResultDF3=ResultDF.rename({'Maths':'Sub1', 'Science':'Sub2','English':'Sub3', 
            'Hindi':'Sub4'}, axis='index')
print(ResultDF3)
print()

ResultDF4=ResultDF.rename({'Maths':'Sub1','Science':'Sub2','Hindi':'Sub4'}, axis='index')
print(ResultDF4)
print()

#Renaming Column Labels of a DataFrame
ResultDF5=ResultDF.rename({'Arnab':'Student1','Ramit':'Student2',
                          'Samridhi':'Student3','Mallika':'Student4'},
                         axis='columns')
print(ResultDF5)
print()

#Accessing DataFrames Element through Indexing
#print(ResultDF.loc['science'])
print()

print(ResultDF.loc[:,'Arnab'])
print()


#Boolean Indexing
print(ResultDF.loc['Maths'] > 90)
print()

print(ResultDF.loc[:,'Arnab']>90)
print()


#Accessing DataFrames Element through Slicing
print(ResultDF.loc['Maths': 'Science'])
print()

print(ResultDF.loc['Maths': 'Science', 'Arnab'])
print()

print(ResultDF.loc['Maths': 'Science', 'Arnab':'Samridhi'])
print()

print(ResultDF.loc['Maths': 'Science',['Arnab','Samridhi']])
print()

#Filtering Rows in DataFrames
#print(ResultDF.loc[[True, False, True]])
print()

#Joining, Merging and Concatenation of DataFrames
dFrame1=pd.DataFrame([[1, 2, 3], [4, 5], [6]], columns=['C1', 'C2', 'C3'],
                     index=['R1', 'R2', 'R3'])
print(dFrame1)
print()

dFrame2=pd.DataFrame([[10, 20], [30], [40, 50]], columns=['C2', 'C5'],
                     index=['R4', 'R2', 'R5'])
print(dFrame2)
print()

dFrame3=dFrame1.append(dFrame2)
print(dFrame3)
print()

#Attributes of DataFrames
ForestArea = {'Assam' :pd.Series([78438, 2797, 10192, 15116],
        index = ['GeoArea', 'VeryDense', 'ModeratelyDense', 'OpenForest']),
             'Kerala' :pd.Series([ 38852, 1663, 9407, 9251],
        index = ['GeoArea' ,'VeryDense', 'ModeratelyDense', 'OpenForest']),
             'Delhi' :pd.Series([1483, 6.72, 56.24, 129.45],
        index = ['GeoArea', 'VeryDense', 'ModeratelyDense', 'OpenForest'])}
ForestAreaDF = pd.DataFrame(ForestArea)
print(ForestAreaDF)
print()

print(ForestAreaDF.index)
print()

print(ForestAreaDF.columns)
print()

print(ForestAreaDF.dtypes)
print()

print(ForestAreaDF.values)
print()

print(ForestAreaDF.shape)
print()

print(ForestAreaDF.size)
print()

print(ForestAreaDF.T)
print()

print(ForestAreaDF.head(2))
print()

print(ForestAreaDF.tail(2))
print()

print(ForestAreaDF.empty)
print()
