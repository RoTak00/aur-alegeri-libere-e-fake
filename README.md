# UPDATE 09.12

Un coleg anonim de pe reddit a pus la dispozitie un script care permite colectarea datelor in momentul in care site-ul le cere in mod uzual, undeva la 20 de secunde.

Astfel, colectarea datelor a putut continua si astazi, cu 800 de esantioane de la 11:11:00 9.12.24 pana la 18:34:00.

### AUR a creat o petitie cu informatii fake

Site-ul [Alegerilibere](https://alegerilibere.ro/index.html) pretinde ca afiseaza numarul de semnaturi stranse.

Acest script .sh face un request periodic pentru a prelua numarul de semnaturi din API-ul site-ului.

Datele existente incep de la 2024-12-07 20:26:34

Script-ul python face regresie liniara si compara rezultatele colectate cu o linie dreapta.

Se observă că datele legate de numărul de semnături sunt, de fapt, incrementate periodic și exact, și deci nu corespund cu un număr adevărat de semnături strânse

## HOW TO USE

### Requirements

- Python 3.x
- Pandas, Matplotlib, Scipy

```
pip install pandas matplotlib scipy
```

### Rulare

```
python3 test.py [fisier] [nr_esantioane] [offset_esantioane]
```

#### Argumente

1. [fisier] - by default, fisierul testat va fi output.csv, dar acesta contine multe date preluate la intervale diferite de timp. Recomand rularea cu fisierele batch_1.csv (20:26 - 23:54), batch_2.csv (00:37 - 01:03) sau batch_3.csv (09:59 - 10:13).
2. [nr_esantioane] - by default, None, deci se folosesc toate datele din fisier. Se poate folosi o valoare cum ar fi 500 pentru a se observa cresterea clar liniara pe intervale mai scurte de timp
3. [offset_esantioane] - by default, None, deci se incepe de la 0. Se poate folosi in combinatie cu nr_esantioane pentru a studia cresterea pe diferite intervale de timp a nr. de semanturi

### Exemple rulare

`python3 test.py batch_1.csv 500`

![500 de esantioane din primul batch](imagini/fig1.png)

`python3 test.py batch_2.csv 500`

![500 de esantioane din al doilea batch](imagini/fig2.png)

`python3 test.py batch_3.csv`

![Esantioanele din al treilea batch](imagini/fig3.png)

`python3 test.py batch_3.csv`

![Esantioanele din al treilea batch](imagini/fig3.png)

`python3 test.py batch_1.csv 1000 1000`

![1000 de Esantioane, offset cu 1000, din primul batch](imagini/fig4.png)

## UPDATE

Server-ul da raspuns foarte foarte incet, pot colecta date doar la ~10 secunde. Reparat script-ul pentru a avea in vedere diferentele de timp. E o linie dreapta 100% din nou.

## UPDATE

Site-ul a fost inchis o perioada incepand cu ora 01:00 08.12.2024, si redeschis dimineata. Colectarea datelor a reinceput la ora 09:59

## UPDATE

08.12.2024 18:38 - de la ora 17:58, numarul de semnaturi s-a oprit la 839272 si site-ul nu mai e responsiv.

## UPDATE

E pus acum cloudflare pe site, dar API call-ul care ar trebui sa intoarca numarul de semnaturi esueaza cu 500 internal server error.
