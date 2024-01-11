Analiză și Vizualizare Date din Fișierul CSV

Cerinta: Se considera fisierul data.csv atasat.

Sa se importe valorile din fisier si sa se ploteze (si afiseze grafic)

* toate valorile

* primele X valori

* ultimele Y valori pentru coloanele Durata si Puls.

->Acest proiect Python utilizează bibliotecile pandas și matplotlib pentru a importa datele dintr-un fișier CSV și a crea diagrame pentru analiză vizuală.

-Instrucțiuni
1.Descărcați fișierul data.csv și asigurați-vă că se află în același director cu script-ul Python.

2.Instalați bibliotecile necesare, dacă nu le aveți deja, folosind următoarea comandă:
pip install pandas matplotlib
3.Folosiți următorul cod în script-ul dvs. Python:


import pandas as pd
import matplotlib.pyplot as plt

- Numele fișierului CSV
nume_fisier = 'data.csv'

- Încărcarea datelor din fișierul CSV
date = pd.read_csv(nume_fisier)

- Plotează toate valorile
date.plot()
plt.title('Toate valorile')
plt.show()

- Plotează primele X valori
X = 4
date.head(X).plot()
plt.title(f'Primele {X} valori')
plt.show()

- Plotează ultimele Y valori pentru coloanele Durata și Puls
Y = 15
date[['Durata', 'Puls']].tail(Y).plot()
plt.title(f'Ultimele {Y} valori pentru Durata și Puls')
plt.show()
Executați script-ul Python pentru a importa datele din fișierul CSV și a genera diagramele.

Diagramele vor fi afișate în fereastra de vizualizare.

Explicarea Codului
Se utilizează biblioteca pandas pentru încărcarea datelor din fișierul CSV într-un cadru de date.
Se utilizează matplotlib.pyplot pentru a plota diagramele.
Se creează trei diagrame diferite:
Toate valorile din fișierul CSV.
Primele X valori din setul de date.
Ultimele Y valori pentru coloanele 'Durata' și 'Puls'.
Modificați variabilele X și Y conform nevoilor dvs. pentru a ajusta numărul de valori afișate în diagrame.





