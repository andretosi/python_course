| Classe                 | Attributi obbligatori                                                                     | Metodi minimi                                          |
| ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Persona**            | `nome`, `cognome`, `anno_nascita`, `codice` (id univoco)                                  | `full_name()`, `eta(anno_corrente)`, `as_dict()`       |
| **Esame**              | `nome`, `crediti`, `voto` (0‑30)                                                          | `superato() → bool`, `__str__()`                       |
| **Studente (Persona)** | **tutti** quelli di `Persona` + `corso_di_studi`, `matricola`, `esami` (lista di `Esame`) | `aggiungi_esame(ex)`, `media_ponderata()`, `__str__()` |
