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

<a href="{{ site.url }}/downloads/fourier-0.1.py" class="button">
  Scarica<br/>
  <small>fourier-0.1.py | 2.6 kB</small>
</a>

#### Dipendenze

Lo script ha bisogno delle seguenti librerie per funzionare:

 * [Matplotlib](http://matplotlib.org/)
 * [Numpy and Scipy](http://www.scipy.org/)

Su Ubuntu 14.04 (e precedenti) è sufficiente eseguire questo comando per installarle:

    sudo apt-get install python-matplotlib python-numpy python-scipy

Per altri sistemi operativi si faccia riferimento ai siti delle rispettive librerie.

#### Come usarlo

È sufficiente aprire un terminale nella cartella dov'è stato scaricato lo script ed eseguire:

    python fourier.py

Lo script mostra un animazione della corda pizzicata. Inoltre genera un video `fourier.mp4`
in modo da poter visualizzare l'animazione senza dover ricalcolare tutti i passi. Sul mio PC
(processore Celeron 1.3 GHz) impiega circa 30 secondi a elaborare l'animazione.

Purtroppo lo script funziona solo con la versione 2.7 di python poichè, in python 3, numpy da un errore
al momento del salvataggio del video.



### La matematica

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

Voglio anche descrivere brevemente com'è possibile ottenere una descrizione matematica di
come si comporta una corda pizzicata. Questa è la matematica implementata nel programmino.

La sezione è spezzata in 2 parti: nella prima è descritto come risolvere l'equazione
delle onde, mentre nel secondo ho applicato le soluzioni trovate al problema della
corda pizzicata.

#### Soluzioni dell'equazione delle onde

L'equazione che governa il comportamento delle perturbazioni su una fune è la famosa **equazione delle onde**,
che si può ricavare dalla seconda legge di Newton:

$$ \frac{\partial^2 f}{\partial x^2} - \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2} = 0 $$

In questa equazione \\( f = f(x, t) \\) indica lo spostamento della corda dalla posizione di equilibrio,
che non deve essere troppo grande (approssimazione che si fa per ricavare l'equazione).
Tra tutte le soluzioni che l'equazione delle onde ammette (si può calcolare la soluzione generale,
ma non è semplicissimo), a noi interessano le soluzioni **separabili**. Le soluzioni separabili
sono funzioni con la seguente forma:

$$ f(x, t) = g(x)h(t) $$

Queste soluzioni possono sembrare molto particolari e in effetti lo sono. Tuttavia occorre ricordare
che l'equazione delle onde è omogenea e quindi la somma di soluzioni è a sua volta soluzione.
Questo fatto, unito alle serie di Fourier, ci permetterà di trovare la soluzione generale.

Imponendo che la soluzione sia separabile e inserendola nell'equazione si ottiene:

$$ \frac{\partial^2 g(x)}{\partial x^2}h(t) = \frac{1}{v^2}\frac{\partial^2 h(t)}{\partial t^2}g(x) $$

o meglio

$$ \frac{v^2}{g(x)}\frac{\partial^2 g(x)}{\partial x^2} = \frac{1}{h(t)}\frac{\partial^2 h(t)}{\partial t^2} = \text{costante} $$

I due termini devono essere costanti perchè altrimenti mantenendo la stessa posizione (mantenendo fisso x) ma spostandosi ad un altro
istante (variando t), l'uguaglianza non varrebe più. La costante può essere positiva (si avranno allora soluzioni
**iperboliche**, ovvero un esponenziale che va all'infinito), oppure negativa (per cui si ottengono soluzioni
**periodiche**, ovvero soluzioni sinusiodali). A noi chiaramente interessano le soluzioni periodiche, poichè quelle
iperboliche non hanno significato fisico.

Imponiamo quindi che la costante valga \\(-\omega^2\\) (in seguito si vedrà che questa costante è proprio
una pulsazione, per cui ho scelto la lettera \\(\omega\\)). 

$$ \frac{\partial^2 g(x)}{\partial x^2} = -\frac{\omega^2}{v^2}g(x) \qquad \text{e} \qquad \frac{\partial^2 h(t)}{\partial t^2} = -\omega^2 h(t) $$

Le soluzione sono facilmente individuabili e sono

$$ g(x) = G\cos(\frac{w}{v}x + \phi) \qquad \text{e} \qquad h(t) = H\cos(wt + \psi) $$

come si può facilmente verificare (Chiaramente sostituendo il coseno con un seno non cambia nulla
poiché seno e coseno sono essenzialmente la stessa funzione traslata di \\(\pi/2\\). Questa possibilità è inclusa
nelle costanti \\( \phi \;\text{e}\; \psi \\). Sono inoltre incluse le combinazioni lineari di seni e coseni,
che possono sempre essere scritte come un singolo seno o coseno, utilizzando le formule di addizione.).

Ora possiamo ricostruire la soluzione:

$$ f(x, t) = g(x)h(t) = G\cos(\frac{w}{v}x + \phi)  H\cos(wt + \psi)$$

Come tutte le equazioni differenziali, è necessario imporre delle condizioni iniziali per determinare le costanti
nella soluzione. Vedremo come fare nella prossima sezione!

La soluzione ha una proprietà notevole: nei punti dove \\( \cos(\frac{w}{v}x + \phi) = 0 \\), la
soluzione è nulla per tutti i tempi. Questi punti si chiamano **nodi**.

#### Il problema della corda pizzicata.

Supponiamo di avere una corda tesa come in <a href="#fig1">Figura 1</a>, pizzicata nel punto a, con 0 < a < L.
La fune viene spostata dall'equilibrio di una distanza h e poi, al tempo t = 0, viene lasciata.
Il programmino mostra quello che succede di seguito, e voglio ricavarlo qui, in formule.

<table class="sidecap"><tr>
  <td>
    <img src="{{ site.url }}/images/fourier/corda_pizzicata.svg" height="360" />
  </td>
  <td class="caption">
    <a name="fig1">Figura 1</a>
    La figura mostra la corda all'istante iniziale. In questo istante la corda viene rilasciata.
    Il nostro compito è calcolare come vibrerà la fune col passare del tempo. La dimensione verticale
    è esagerata (l'eq. delle onde vale solo per piccoli scostamenti dalla posizione di equilibrio,
    cioè per h piccoli).
  </td>
</tr></table>

La posizione della corda deve evidentemente soddisfare l'equazione delle onde. Abbiamo che:

$$ f(x, 0) = \begin{cases} \frac{h}{a} x & 0 < x < a \\\ \frac{h(L - x)}{L - a} & a < x < L \end{cases} $$

PAGINA DA COMPLETARE