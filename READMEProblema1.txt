Sistem de Management al Angajaților
-Cerinata:
 Se considera fisierul employee.py. Atasat. Creați o clasă care va moșteni clasa Employee – clasa Manager.
· Numarul de obiecte create din clasa Manger va fi păstrat în variabila de clasă mgr_count
· Constructorul clasei va avea 3 argumente: name, salary si department
 La departament veti prefixa numele echipei voastre de la disciplina
· Dacă X%3==0 În clasa Manager, modificați metoda ‘display_employee’ a.î. să afișeze doar numele angajatului.
· Dacă X%3==1 În clasa Manager, modificați metoda ‘display_employee’ a.î. să afișeze doar salariul angajatului.
· Dacă X%3==2 În clasa Manager, modificați metoda ‘display_employee’ a.î. să afișeze doar departamentul angajatului.
· Creați Y/3 obiecte ale clasei Manager. Apelați metoda ‘display_employee’ pentru toate obiectele din clasa Manager și pentru obiectele din clasa Employee.
· Afișați valoarea atributului emp_count pentru o instanță a clasei Employee și pentru una a clasei Manager.

->Acest script Python implementează un simplu Sistem de Management al Angajaților cu două clase: Employee și Manager. Clasa Manager este derivată din clasa Employee și introduce funcționalități suplimentare.

-Clasa Employee
Clasa Employee servește ca o clasă de bază comună pentru toți angajații. Include următoarele atribute și metode:

-Atribute:
empCount: O variabilă de clasă care ține evidența numărului total de angajați.
-Metode:
__init__(self, name, salary, department): Metodă constructor pentru a inițializa un angajat cu un nume, salariu și departament.
display_emp_count(self): Afișează numărul total de angajați.
display_employee(self): Afișează detaliile angajatului, inclusiv nume, salariu și departament.
__del__(self): Metodă destructor pentru a decrementa numărul total de angajați când o instanță este ștearsă.
update_salary(self, new_salary): Actualizează salariul angajatului.
modify_task(self, task_name, status="New"): Modifică lista de sarcini a angajatului.
display_task(self, status): Afișează sarcinile cu un anumit status.

-Clasa Manager
Clasa Manager este derivată din clasa Employee și introduce următoarele modificări:

-Atribute:
mgr_count: O variabilă de clasă care ține evidența numărului total de manageri.
-Metode:
__init__(self, name, salary): Metodă constructor pentru a inițializa un manager cu un nume, salariu și un departament implicit ("D06").
display_employee(self): Suprascrie metoda de afișare în funcție de condiții specifice (X%3) pentru a afișa doar numele, salariul sau departamentul.