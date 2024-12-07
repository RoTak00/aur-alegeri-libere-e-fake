### AUR a creat o petitie cu informatii fake

Site-ul [Alegerilibere](https://alegerilibere.ro/index.html) pretinde ca afiseaza numarul de semnaturi stranse.

Acest script .sh face un request periodic pentru a prelua numarul de semnaturi din API-ul site-ului.

Datele existente incep de la 2024-12-07 20:26:34

Script-ul python face regresie liniara si compara rezultatele colectate cu o linie dreapta.

Se observă că datele legate de numărul de semnături sunt, de fapt, incrementate periodic și exact, și deci nu corespund cu un număr adevărat de semnături strânse

## UPDATE

Chiar daca datele totale de la 20:26:34 nu se mai potrivesc cu o linie dreapta, regresia pentru date de la 20:36 (v1.csv) arata clar o noua linie dreapta. Posibil sa se fi schimbat valoarea de incrementare.
