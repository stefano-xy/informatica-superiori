# Materiale didattico per corsi di informatica di scuola secondaria superiore

Materiale didattico usato nell'anno scolastico 2021-2022
in alcune classi di scuola secondaria superiore presso
l'[I.O. De Gasperi - Battaglia](https://www.comprensivonorcia.edu.it) di Norcia (PG).

Argomenti trattati:

- Algoritmi tramite Flowgorithm
- Conversione dei suddetti algoritmi in python
- Introduzione alla programmazione tramite C++
- Esercizi relativi

Autore: [Stefano Pettini](https://www.linkedin.com/in/pettini).
Contattatemi se il materiale vi è utile o per collaborare.

# Il materiale didattico

Tutto il materiale è visibile all'indirizzo [informatica.pettini.eu](https://informatica.pettini.eu).

## Come modificare i contenuti

Il materiale è pubblicato tramite _GitHub Pages_ all'indirizzo indicato sopra
ed è aggiornato automaticamente a ogni commit. Per contribuire, aprire una PR.

Il sito è generato tramite [Jekyll](https://jekyllrb.com).
Per maggiori informazioni, consultare la relativa guida di
[GitHub Pages](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll).

Ogni file markdown `.md` è scansionato e trasformato in una pagine HTML automaticamente.
Sono inclusi anche i file in sottodirectory. L'homepage è contenuta in `index.md`.

Per ulteriori dettagli su come scrivere un sito web statico tramite _Jekyll_,
consultare la [documentazione ufficiale](https://jekyllrb.com/docs).

## Come riprodurre il sito in locale

Per generare e testate il sito in locale è necessario avere un ambienti di sviluppo _Ruby_ con _Bundler_.

### Installare Ruby, Bundler e Jekyll

Su _Ubuntu_ o _Debian_:

```
sudo apt install bundler ruby-dev zlib1g-dev
```

Gli ultimi due pacchetti sono necessari per compilare alcune dipendenze.

Su _MacOS_ o _Windows_, seguire le istruzioni di installazione di _Ruby_ e _Bundler_
come suggerito nella [guida di installazione](https://jekyllrb.com/docs/installation) di _Jekyll_.

Una volta che _Ruby_ and _Bundler_ sono installati, usare i seguenti comandi per
configurare _Bundler_ e installare le gemme, inclusa la versione corretta di _Jekyll_:

```
bundle config --local path vendor/bundle
bundle install
```

Questi comandi creano le directory `.bundle` e `vendor`,
che *non* devono essere incluse nel _git repository_.

### Generare e testare il sito in locale

Per generare, testare e servire il sito in locale, eseguire:

```
bundle exec jekyll serve
```

Potete poi aprire il sito in locale su [localhost:4000](http://localhost:4000).
