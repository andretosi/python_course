# LA SPESA PER UNA MERENDA
# Vuoi preparare una macedonia e una limonata per una merenda tra amici.
# Scriverai una funzione che decide cosa manca in casa.
# Il codice in fondo userà il suo risultato per calcolare la spesa.

# DATI INIZIALI
# Quantità in pezzi. Prezzi e budget in centesimi di euro.
# necessari indica quanti pezzi servono IN TOTALE, compresi quelli già in casa.
# Ogni ingrediente compare in tutti i dizionari. I dati sono già validi:
# quantità, prezzi e budget sono interi non negativi.

ingredienti = ["mele", "banane", "limoni"]
necessari = {"mele": 4, "banane": 2, "limoni": 2}
in_casa = {"mele": 1, "banane": 3, "limoni": 0}
prezzi = {"mele": 50, "banane": 40, "limoni": 30}
budget = 300


# LA FUNZIONE DA SCRIVERE
# Usa questa firma, aggiungendo il corpo della funzione:
# def crea_lista_spesa(ingredienti, necessari, in_casa):
#
# La funzione riceve i nomi da controllare, le quantità necessarie e quelle
# già presenti. Deve RESTITUIRE un nuovo dizionario con soltanto gli
# ingredienti da comprare e le quantità mancanti.
# Se servono 4 mele e ne hai 1, la voce da restituire è "mele": 3.
# Se un ingrediente basta o avanza, non deve comparire nel risultato.
# Se hai già tutto, oppure ingredienti è una lista vuota, restituisci {}.
#
# Usa i parametri ricevuti: la funzione deve funzionare anche con altri dati.
# Non modificare le liste o i dizionari ricevuti. Crea un nuovo dizionario.
# La funzione non deve stampare: restituisci il risultato con return.
# Prezzi e budget servono al codice successivo, non a questa funzione.
# Ricorda: return termina la chiamata. Devi prima controllare tutti gli
# ingredienti, non fermarti dopo il primo.
#
# SCRIVI QUI LA TUA FUNZIONE, PRIMA DEL BLOCCO DI UTILIZZO.



# COME PROVARLA
# Quando la funzione è pronta, decommenta SOLO il codice tra i due marcatori
# INIZIO CODICE DI UTILIZZO e FINE CODICE DI UTILIZZO qui sotto.
# Per decommentare, elimina il primo "# " da ciascuna riga del blocco.
# Mantieni gli altri spazi: i rientri dentro for e if fanno parte del codice.
# Lascia commentate le istruzioni, i marcatori e il risultato atteso.
# Salva il file e, dal terminale aperto nella stessa cartella, esegui:
# python3.13 spesa.py
# Prima di scrivere la funzione e attivare il blocco, il file non stampa nulla.
#
# RISULTATO ATTESO CON I DATI INIZIALI
# Lista della spesa: {'mele': 3, 'limoni': 2}
# Costo: 210 centesimi
# Budget sufficiente
#
# ALTRE PROVE
# Con budget = 210 il budget basta; con 209 no. La lista resta la stessa.
# Ripristina budget = 300 e metti 10 pezzi di ogni ingrediente in in_casa:
# il risultato della funzione deve essere {}, con costo zero.
# Se in_casa contiene zero per ogni ingrediente, servono 4 mele, 2 banane
# e 2 limoni: il costo è 340 e il budget di 300 non basta.
# Poi prova a chiamare la funzione con dati diversi, senza cambiarne il corpo.

# INIZIO CODICE DI UTILIZZO
# lista_spesa = crea_lista_spesa(ingredienti, necessari, in_casa)
#
# totale = 0
# for nome in lista_spesa:
#     totale = totale + lista_spesa[nome] * prezzi[nome]
#
# print("Lista della spesa:", lista_spesa)
# print("Costo:", totale, "centesimi")
#
# if totale <= budget:
#     print("Budget sufficiente")
# else:
#     print("Budget insufficiente")
# FINE CODICE DI UTILIZZO
