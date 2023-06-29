import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance .csv')
print(df.head())

female_math = df[df['gender']=='female']['math score'].mean()
male_math = df[df['gender']=='male']['math score'].mean()
female_reading = df[df['gender']=='female']['reading score'].mean()
male_reading = df[df['gender']=='male']['reading score'].mean()
female_write = df[df['gender']=='female']['writing score'].mean()
male_write = df[df['gender']=='male']['writing score'].mean()


print('Результат по математике:', 'Девочки', round(female_math, 2), 'Мальчики:', round(male_math, 2) )
print('Результат по чтению :', 'Девочки', round(female_reading, 2), 'Мальчики:', round(male_reading, 2) )
print('Результат по письму:', 'Девочки', round(female_write, 2), 'Мальчики:', round(male_write, 2) )

s = pd.Series(data = [female_math, male_math, female_reading, male_reading, female_write, male_write],
index = ['Матемю девочки', 'Матем мальчики', 'Чтение девочки','Чтение мальчики','Письмо девочки','Письмо мальчики'])
s.plot(kind = 'barh', grid = True)
plt.show()