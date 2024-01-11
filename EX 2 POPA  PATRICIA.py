import pandas as pd
import matplotlib.pyplot as plt

nume_fisier = 'data.csv'
date = pd.read_csv(nume_fisier)

date.plot()
plt.title('Toate valorile')
plt.show()

X = 4
date.head(X).plot()
plt.title(f'Primele {X} valori')
plt.show()

Y = 15
date[['Durata', 'Puls']].tail(Y).plot()
plt.title(f'Ultimele {Y} valori pentru Durata și Puls')
plt.show()
