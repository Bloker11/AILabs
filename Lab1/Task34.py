import matplotlib.pyplot as plt
import pandas as pd


miasta = pd.read_csv("miasta.csv")
print(miasta)

df = pd.DataFrame({'Rok': [2010], 'Gdansk': [460], 'Poznan': [555], 'Szczecin': [405]})

# df.to_csv('miasta.csv', mode='a', index=False, header=False)
plt.plot(miasta['Rok'], miasta['Gdansk'], color='r', marker='o', label='Gdansk')
plt.plot(miasta['Rok'], miasta['Poznan'], color='b', marker='o', label='Poznan')
plt.plot(miasta['Rok'], miasta['Szczecin'], color='y', marker='o', label='Szczecin')
plt.xlabel('Years')
plt.ylabel('Popularity')
plt.title('Popularity in major polish cities')
plt.legend()
plt.show()