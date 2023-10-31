import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

basepath = r'C:\Users\Winthrop Isaac\OneDrive\Documents\GitHub\TanzaniaProject\FinalCSVs\TeacherTrainingExam20-23.csv'

df = pd.read_csv(basepath, index_col=False)
print(df.head(10))

##GRAPHING GPA
#Remove non-numeric entries
df = df[pd.to_numeric(df['AGGT'], errors ='coerce').notnull()]
#Make the remaining entries numeric
df['AGGT'] = pd.to_numeric(df['AGGT'])
summary = df['AGGT'].mean()
print(f'The mean score among students is: ', summary)
graph = df['AGGT'].plot(kind='kde')
plt.show()

##GRAPH GPA DENSITY BY GENDER
plt.clf()
data = df[['AGGT','SEX']]
sns.set_style('whitegrid')
sns.kdeplot(data=data, x = 'AGGT', hue = 'SEX', fill = True, common_norm=False)

plt.xlabel('GPA')
plt.ylabel('Density')
plt.title('Density Plot of GPA by Gender')

plt.show()

##GRAPH GPA DENSITY BY YEAR
plt.clf()
data = df[['AGGT','Year']]
sns.set_style('whitegrid')
sns.kdeplot(data=data, x = 'AGGT', hue = 'Year', fill = True, common_norm=False)

plt.xlabel('GPA')
plt.ylabel('Density')
plt.title('Density Plot of GPA by Year')

plt.show()