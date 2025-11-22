# Materiale didattico per corsi di informatica di scuola secondaria superiore

Materiale didattico è stato usato a partire dell'anno scolastico 2021-2022
in alcune classi di scuola secondaria superiore dei seguenti indirizzi:

- **2INF** - informatico
- **2TUR** - turistico
- **3SIA** - sistemi informativi aziendali

Alcuni argomenti trattati:

- Sistema di numerazione binario e esadecimale, conversioni.
- Algoritmi tramite Flowgorithm e Flowrun.
- Conversione dei suddetti algoritmi in _python_.
- Pagine web con _HTML_, _CSS_, _JavaScript_.
- Introduzione alla programmazione tramite _C++_.
- Esercizi relativi.

Autore: [Stefano Pettini](https://www.linkedin.com/in/pettini).
Contattatemi se il materiale vi è utile o per collaborare.

# Il materiale didattico

Tutto il materiale è visibile all'indirizzo [informatica.pettini.eu](https://informatica.pettini.eu).

## Come modificare i contenuti

Il materiale è pubblicato tramite _GitHub Pages_ all'indirizzo indicato sopra
ed è aggiornato automaticamente a ogni commit. Per contribuire, aprire una PR su _GitHub_.

Il sito è generato tramite [Jekyll](https://jekyllrb.com).
Per maggiori informazioni, consultare la relativa guida di
[GitHub Pages](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll).

Ogni file markdown `.md` è scansionato e trasformato in una pagine HTML automaticamente.
Sono inclusi anche i file in sottodirectory. L'homepage è contenuta in `docs/index.md`.

Per ulteriori dettagli su come scrivere un sito web statico tramite _Jekyll_,
consultare la [documentazione ufficiale](https://jekyllrb.com/docs).

## Come riprodurre il sito in locale

Per generare e testate il sito in locale è necessario avere un ambiente di sviluppo _Ruby_ con _Bundler_.

### Installare Ruby, Bundler e Jekyll

Su _Linux_, sia _Ubuntu_ che _Debian_:

```
sudo apt install bundler ruby-dev zlib1g-dev
```

Gli ultimi due pacchetti sono necessari per compilare alcune dipendenze.

Su _macOS_:

```
brew install ruby
```

Seguire le istruzioni visualizzate per modificare `PATH` in `.zshrc`.
Chiudere e riaprire il terminale, verificare che Ruby 3 sia installato con `ruby --version`.

Su _Windows_, seguire le istruzioni di installazione di _Ruby_ e _Bundler_
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
