---
layout: post
categories: it science physics waves
---

Un paio di giorni fa, invece di studiare le onde elettromagnetiche,
mi sono perso nello scrivere un programmino in python che mostra come vibra una corda pizzicata,
e ho pensato di condividelo qui. Le ore di studio ormai sono perse comunque!

In realtà l'idea non è originale, anzi l'ho copiata dal mio prof. di
Fisica Generale 3, che aveva usato un programmino simile (ma scritto in Matlab)
per spiegarci l'equazione delle onde.

### Per gli impazienti

Lo script è distribuito sotto licenza GPL 3.

<a href="{{ site.url }}/downloads/fourier-0.1.py" class="button">Scarica<br/>
<small>fourier-0.1.py | 2.6 kB</small></a>

#### Dipendenze

Lo script ha bisogno delle seguenti librerie per funzionare:

 * [Matplotlib](http://matplotlib.org/)
 * [Numpy and Scipy](http://www.scipy.org/)

Su Ubuntu 14.04 (e precedenti) è sufficiente eseguire questo comando per installarle:

    sudo apt-get install python-matplotlib python-numpy python-scipy

Per altri sistemi operativi si faccia riferimento ai siti delle rispettive librerie.
