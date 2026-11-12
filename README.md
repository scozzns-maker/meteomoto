# MeteoMoto

Meteo ora per ora (9–18) per 40 località da giro in moto (10 per regione) di Marche, Umbria, Abruzzo e Toscana, con verdetto «Si va / Con prudenza / Garage».

Pagina: https://scozzns-maker.github.io/meteomoto/

La pagina si aggiorna da sola, senza interventi esterni:

- **Previsioni**: lette da [Open-Meteo](https://open-meteo.com/) nel browser a ogni apertura (dati CC BY 4.0); se l'ultima lettura ha meno di 10 minuti si riusa quella. Modello ICON-2I di ItaliaMeteo-ARPAE (2 km) per i giorni che copre, altrimenti il miglior modello disponibile; probabilità di pioggia dai modelli d'insieme.
- **Allerte**: [Meteoalarm](https://www.meteoalarm.org) (Servizio Meteorologico dell'Aeronautica Militare). Il feed non si può leggere dal browser, quindi lo legge GitHub Actions ogni 30 minuti (`.github/workflows/allerte.yml`) e lo salva in `alerts.json`, solo quando cambia o almeno ogni 6 ore.

File:

- `index.html`: la pagina (mappa animata ora per ora, mattina e pomeriggio, dettaglio per località).
- `icon.svg`, `icon-*.png`, `og.png`, `manifest.webmanifest`: logo, icone per la schermata Home e anteprima dei link condivisi.
- `alerts.json`: allerte Meteoalarm di Marche, Umbria, Abruzzo e Toscana, scritte da GitHub Actions.
- `.github/scripts/allerte.py`: lo script che legge Meteoalarm (solo libreria standard di Python).

Nota: GitHub sospende le azioni programmate dopo 60 giorni senza attività nel repository. I salvataggi periodici di `alerts.json` contano come attività; se l'azione risultasse sospesa, si riattiva da Actions → Allerte Meteoalarm → Enable workflow.
