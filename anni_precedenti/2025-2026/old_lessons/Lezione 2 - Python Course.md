**Lezione 2 (26/03)**
- Data Types 1 e relativi metodi (Test su Python da Terminale):
	- Booleans
	- Integers
	- Floats
	- Stringhe 
- If/else/elif
	- Esempi e Programmi Semplici con if else e stringhe
- *Problema: Variabili Booleane, Intere, Float, Stringhe ed If/Else*
- Data Types 2 e relativi metodi:
	- Liste
- For Loops
- *Problema: Liste e Cicli For*
- Culture Pill/esterni

[[Python Course - Lezione 2]]
#### Problema: Variabili Booleane, Intere, Float, Stringhe ed If/Else

```
Scrivi un programma in Python che simuli una semplice valutazione di rischio per un paziente. Il programma dovrà:

1. Chiedere all’utente di inserire:
   • Nome del paziente (es Aldo Rossi).  
   • Età del paziente (es 76).  
   • Valore di pressione arteriosa sistolica (es 107.4)
   • Indicare se il paziente è fumatore o no (es s/n)

2. In base ai valori inseriti, il programma dovrà stampare un messaggio di allerta o di normalità:
   • Se l’età è maggiore di 65, la pressione sistolica è minore a 120, e il paziente è fumatore mostrare un avviso come “Attenzione: il paziente è a possibile rischio ipertensione”.  
   • Se la pressione è superiore a 120 il paziente è a rischio ipertensione.
   • Se l'età è superiore ai 65 anni e la pressione maggiore di 120 il paziente è a grave rischio ipertensione.
   • Altrimenti, mostrare un messaggio di livello normale di rischio.  

3. Alla fine, stampare un riepilogo completo dei dati inseriti (nome, età e valori registrati).  


```


#### Problema: Liste e cicli For
es
```
ESERCIZIO: Calcolo Frequenze Cardiache in un Intervallo

1. Immagina di aver acquisito la frequenza cardiaca (battiti al minuto, bpm) di un paziente ogni minuto per 10 minuti consecutivi. Raccogli questi valori in una lista (puoi sceglierli tu, per esempio [72, 78, 90, 65, 100, 88, 76, 80, 110, 95]).

2. Crea un programma che:
   a) Utilizzi un ciclo for per scorrere la lista e stampare ogni valore di frequenza con l’indicazione di un commento, ad esempio “Frequenza al minuto X: Y bpm”.  
   b) All’interno del ciclo, per ogni battito registrato (ad esempio Y bpm) stabilisci se:
      - È considerato nella norma (tra 60 e 100 bpm).
      - È considerato troppo basso (sotto i 60 bpm).
      - È considerato eccessivo (sopra i 100 bpm).

3. Alla fine del ciclo, calcola e stampa:
   - La frequenza cardiaca media (come numero float).
   - Quanti valori rientrano nella norma e quanti risultano anomali (sommando quelli troppo bassi e quelli eccessivi).

2. Ora tratta questi valori (72, 78, 90, 65, 100, 88, 76, 80, 110, 95) come input dell’utente, convertiti in lista, e ripeti lo stesso procedimento.

Suggerimento: Puoi usare funzioni come `sum()` e `len()` per calcolare la media e variabili contatore per tenere traccia dei battiti cardiaci normali o anomali.
```