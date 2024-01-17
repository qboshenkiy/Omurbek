import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company.csv', delimiter=';', encoding='windows-1251')
print(df)

df.plot(x='Business', y='Revenue', kind='bar', legend=False)
plt.show()
