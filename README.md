# cravattaBot
> TL;DR: Ho fatto un bot telegram per la chat del corso di sistemi.

## Indice
- [Installazione e prerequisiti](https://github.com/takenX10/cravattaBot#Installazione-e-prerequisiti)
    - [Prerequisiti](https://github.com/takenX10/cravattaBot#Prerequisiti)
    - [Installazione](https://github.com/takenX10/cravattaBot#Installazione)
- [Setup](https://github.com/takenX10/cravattaBot#Setup)
    - [Configurazione dati](https://github.com/takenX10/cravattaBot#Configurazione-dati)
    - [Come creare il bot e prendere il token](https://github.com/takenX10/cravattaBot#Come-creare-il-bot-e-prendere-il-token)
    - [Come trovare il chatid](https://github.com/takenX10/cravattaBot#Come-trovare-il-chatid)
- [Esecuzione](https://github.com/takenX10/cravattaBot#Esecuzione)

---

## Installazione e prerequisiti
### Prerequisiti
Utilizzeremo due librerie di python:
- [telepot](https://telepot.readthedocs.io/en/latest/index.html)
- [eel](https://github.com/ChrisKnott/Eel)

puoi eseguire questo comando per installarle direttamente
```console
sudo python3 -m pip install -r requirements.txt
```
oppure installarle singolarmente
```console
sudo python3 -m pip install telepot
sudo python3 -m pip install eel
```
oppure seguire la guida all'installazione dai siti ufficiali [telepot](https://telepot.readthedocs.io/en/latest/index.html#installation) [eel](https://github.com/ChrisKnott/Eel#install)

### Installazione
Basta clonare la repo:
```console
sudo git clone https://github.com/takenX10/cravattaBot
```

## Setup
### Configurazione dati
> **RICORDATI DI SEGUIRE I PASSI SPIEGATI NELL'INSTALLAZIONE**

Come prima cosa configurare i dati all'interno del file `src/botdata.py`, in particolare vanno modificati:

- token -> il token del bot di telegram da prendere dal botfather
- chatid -> l'id della chat dove avverrà il redirect dei messaggi da parte del bot 
    - -1 per non fare redirect
- debug_print -> le print di debug 
    - True o False
- autoscroll ->  Attiva o disattiva l'autoscroll del sito all'ultimo messaggio

### Come creare il bot e prendere il token
Quotando la [documentazione ufficiale di telegram](https://core.telegram.org/bots)

> There's a… bot for that. Just talk to [BotFather](https://t.me/botfather) (described below) and follow a few simple steps.

### Come trovare il chatid
A meno che l'api di telegram venga modificata questi sono i passaggi:
1. Dal client di telegram crea un gruppo e aggiungi dentro il bot
2. Manda un messaggio qualsiasi di prova
3. Apri `https://api.telegram.org/bot<token>/getUpdates` dove sostituisci `<token>` con il token del bot (quindi se il token fosse `ABCD:22AABB` dovresti aprire `https://api.telegram.org/botABCD:22AABB/getUpdates`)
4. All'interno delle info del messaggio dovrebbe essere presente il chat-id del gruppo.

Nel caso di modifiche googla la soluzione, è abbastanza banale in ogni caso.

## Esecuzione
> Ricordati di installare `telepot` e `eel` e di modificare i dati all'interno di `botdata.py`

```console
python3 src/cravattaBot.py
```
