/* 
1) Mostra i 10 film più lunghi presenti nel database,
 ordinandoli dal più lungo al più corto.
 */
 select * from film 
 order by length desc
 limit 10;
 
 /*
2) Qual è il prezzo medio di noleggio (rental_rate)
 di tutti i film? Rinomina il 
 risultato come "Prezzo_Medio_Noleggio".
*/
 select AVG(rental_rate) as Prezzo_Medio_Noleggio
 from film;

/*
3) Nella tabella film, conta quanti film 
ci sono per ogni durata di noleggio (rental_duration).
*/
select rental_duration, count(*) as numero_film
from film 
group by rental_duration;

/*
4) Vai nella tabella payment e conta
 quanti pagamenti ha registrato ogni staff_id.
*/
select staff_id, count(*) as num_pagamenti
from payment 
group by staff_id;
/*
Per ogni customer_id nella tabella
 payment, mostra il pagamento più 
 alto (MAX) e quello più basso (MIN) 
 che abbiano mai effettuato.
*/
select staff_id, Max(amount) as pag_max, min(amount) as pag_min
from payment 
group by staff_id;
