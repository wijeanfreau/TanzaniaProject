import pandas as pd
import matplotlib.pyplot as plt

basepath = 'V:\FHSS-JoePriceResearch\RA_work_folders\Winthrop_Jeanfreau\TanzaniaProject\FinalCSVs\TeacherTrainingExam20-23.csv'

df = pd.read_csv(basepath, index_col=False)
#Remove non-numeric entries
df['AGGT'] = pd.to_numeric(df['AGGT'], errors='coerce')
df['AGGT'] = df['AGGT'].notnull()
summary = df['AGGT'].mean()
print(f'The mean score among students is: ', summary)
graph = df['AGGT'].plot(kind='kde')
print(graph)S