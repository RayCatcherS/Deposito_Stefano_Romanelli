# Appunti mysql Martedì 03



---

##### **Condizione sulla selezione di tuple**



esempio query:

select rental\_id from payment

where amount = 0.99;



dove 

* rental\_id è attributo dello schema della relazione payment
* where è la condizione di selezione delle tuple (condizione su attributo)



---



select rental\_id from payment

where amount = 0.99

order by length DESC;



con ordinamento decrescente rispetto all'attributo length



---

##### **ordine**



select rental\_id from payment

where amount = 0.99

order by length DESC

LIMIT 10;



---

##### **selezione di tuple con valori precisi o meno**



select \* from film

where title like "worst %"



dopo la % ci può essere qualsiasi cosa, non è una coincidenza esatta con la stringa



select \* from film

where title like "% worst %"



può essere anche fatto così per cercare una sotto stringa 



---

##### **Operatori logici**



select \* from film

where length>120 AND rental\_rate<10



oppure 



select \* from film

where length between 60 and 90





oppure 



select \* from film

where rating IN ("G","R")



ovvero solo le tuple che hanno valori stringa "G" o "R"



---

##### **Selezione di tuple con valori distinti**



select distinct rental\_rate from film



prende tutti i possibili valori per la colonna (come se stampasse il dominio dell'attributo)



---

select count(\*) from film;





oppure 



select rating, count(\*) as totale\_film

from film

group by rating





---

##### **Operazioni con raggruppamento**



select custumer\_id, SUM(amount) as totale\_speso

from payment

group by customer\_id





prende tutti gli attributi custumer\_id con lo stesso valore e somma amount, restituisce tuple (totale speso) con customer id univoco e somma degli amount





