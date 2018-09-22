import csv
import pandas as pd

path='aaa.csv'
with open(path) as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)
    
apidict = {x:list(y) for x,y in zip(d[0], zip(*d[1:]))}
df=pd.DataFrame(apidict)
del df['Animal_ID']
del df['Month_Day_Year']
del df['Name']
df=df[df.Animal_Type=='Dog']
suo_count=pd.Series(df['Sex_upon_Outcome']).value_counts()
outcome_count=pd.Series(df['Outcome_Type']).value_counts()
breed_count=pd.Series(df['Breed']).value_counts()