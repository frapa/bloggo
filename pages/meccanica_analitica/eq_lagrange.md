---
layout: default
title: Frapa - Equazioni di Lagrange
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

## Equazioni di Eulero-Lagrange

In questa pagina ricaverò le equazioni di Eulero-Lagrange dal secondo principio
della dinamica. Iniziamo quindi con un sistema di N punti materiali sottoposti
a \\( \ell \\) vincoli (\\(n = 3N - \ell\\) gradi di libertà) e con il secondo
principio

$$ \frac{d}{dt} (m\_i \vec{v}\_i) = \vec{F}\_i + \vec{R}\_i \qquad
\forall i \in {1, \dots, n} $$

dove non ho indicato il riferimento rispetto a cui sono misurate le velocità,
forze e rispetto al quale ha senso l&#39;operazione di derivata. Questo perché
c&#39;è solo un sistema di riferimento. \\(\vec{F}\_i\\) e \\(\vec{R}\_i\\)
sono rispettivamente la risultante delle forze attive (anche quelle inerziali)
e la reazione vincolare agenti sul punto _i_-esimo.

L&#39;idea principale è la seguente: poiché nelle equazioni di Newton entrano anche
le reazioni vincolari che spesso non conosciamo, scriviamo le equazioni con delle
coordinate generalizzate \\(q^1, \dots, q^k\\)
(che prendono già in considerazione l&#39;esistenza di
vincoli). Se i vincoli sono ideali, le reazioni vincolari incognite spariranno
e otterremo delle **equazioni di puro moto** (cioè equazioni che permettono
di calcolare il moto del sistema e in cui non entrano quantità incognite).

In pratica proiettiamo le forze, velocità ed accelerazioni lungo i vincoli,
poiché tanto nella direzione perpendicolare sappiamo già che non ci sarà moto.
(Consiglio di leggere l&#39;[introduzione](introduzione.html) se non lo avete
già fatto).

Prendiamo quindi le componenti di queste quantità e facciamo il prodotto scalare
con i vettori \\(\frac{\partial\vec{x}\_i}{\partial q^k}\\), che sono tangenti ai
vincoli per costruzione. In questo modo otteniamo le componenti delle forze,
velocità ed accelerazioni lungo i vincoli. In formule

$$
\sum\_{i=1}^N \frac{d}{dt} (m\_i \vec{v}\_i) \cdot
\frac{\partial\vec{x}\_i}{\partial q^k} =
\sum\_{i=1}^N \vec{F}\_i \cdot \frac{\partial\vec{x}\_i}{\partial q^k} + 
\sum\_{i=1}^N \vec{R}\_i \cdot \frac{\partial\vec{x}\_i}{\partial q^k}
\qquad \qquad \forall k \in {1, \dots, n} $$

In questa equazione si è considerato il secondo principio della dinamica per
tutti i punti materiali del sistema ed è stato proiettato tutto lungo la
coordinata \\(q^k\\). Al secondo termine riconosciamo le componenti
lagrangiane delle forze attive (vedi
[vincoli\_ideali](vincoli\_configurazioni.html#vincoli\_ideali)). Possiamo quindi
scrivere, assumendo che i vincoli siano ideali,

$$
\sum\_{i=1}^N \frac{d}{dt} (m\_i \vec{v}\_i) \cdot
\frac{\partial\vec{x}\_i}{\partial q^k} =
Q\_k
\qquad \qquad \forall k \in {1, \dots, n} $$

L&#39;equazione precedente, che porta il nome di **equazione simbolica della
dinamica** sarebbe già a posto, anche se la forma non è molto bella. 
Ora sfruttiamo la regola di derivazione di Leibniz (\\( (fg)&#39; = f&#39;g + fg&#39; \\))
al rovescio (\\( f&#39;g = (fg)&#39; - fg&#39; \\) per tentare di scrivere in forma decente
la prima parte dell&#39;equazione

$$
\sum\_{i=1}^N \frac{d}{dt} (m\_i \vec{v}\_i \cdot
\frac{\partial\vec{x}\_i}{\partial q^k}) -
\sum\_{i=1}^N m\_i \vec{v}\_i \cdot
\frac{d}{dt} \frac{\partial\vec{x}\_i}{\partial q^k}
 =
Q\_k
\qquad \qquad \forall k \in {1, \dots, n} $$

Ora dimostriamo un&#39;indentità che ci tornerà utile per semplificare
l&#39;equazione precedente

> **Identità**  Dimostriamo che
> 
> $$ \frac{\partial \vec{x}\_i}{\partial q^k} =
> \frac{\partial \vec{v}\_i}{\partial \dot{q}^k} $$
> 
> dove il punto indica la derivata temporale totale.
> Cominciamo con scrivere la velocità in funzione della posizione:
> 
> $$ \vec{v}\_i = \frac{d\vec{x}\_i}{dt} =
> \frac{\partial \vec{x}\_i}{\partial t} +
> \sum\_{j=1}^n \frac{\partial \vec{x}\_i}{\partial q^j}
> \frac{\partial q^j}{\partial t} =
> \frac{\partial \vec{x}\_i}{\partial t} +
> \sum\_{j=1}^n \frac{\partial \vec{x}\_i}{\partial q^j}
> \dot{q}^j $$
> 
> In pratica abbiamo espresso la derivata totale del tempo in termini di
> derivate parziali nel tempo e nello spazio. Ora deriviamo la velocità per
> \\(\dot{q}^k\\) (per inciso ricordo che \\(\vec{x}\_i \\) è una funzione di
> t e delle varie \\(q^k\\), mentre la velocità dipende anche dalle
> \\( \dot{q}^k \\), come dimostrato nella formula sopra).
> 
> $$ \frac{\partial \vec{v}\_i}{\partial \dot{q}^k} =
> \frac{\partial}{\partial \dot{q}^k} \frac{\partial \vec{x}}{\partial t} +
> \sum\_{j=1}^n \frac{\partial \vec{x}\_i}{\partial q^j}
> \frac{\partial \dot{q}^j}{\partial \dot{q}^k} =
> \frac{\partial \vec{x}\_i}{\partial q^k} $$
> 
> L&#39;ultima uguaglianza deriva dal fatto che sopravvive solo il termine in
> \\(q^k\\) poiché \\(\vec{x}\_i\\) non dipende dalle variabili puntate.

Riprendiamo quindi l&#39;ultima equazione e la riscriviamo utilizzando l&#39;identità
appena provata e l&#39;uguaglianza

$$ \frac{d}{dt} \frac{\partial \vec{x}\_i}{\partial q^k} =
\frac{\partial \vec{v}\_i}{\partial q^k} $$

che è derivata dalla definizione di velocità. Si ottiene quindi

$$
\sum\_{i=1}^N \frac{d}{dt} (m\_i \vec{v}\_i \cdot
\frac{\partial\vec{v}\_i}{\partial \dot{q}^k}) -
\sum\_{i=1}^N m\_i \vec{v}\_i \cdot \frac{\partial\vec{v}\_i}{\partial q^k}
 =
Q\_k
\qquad \qquad \forall k \in {1, \dots, n} $$

Portando fuori le derivate (e aggiungendo 1/2 per far tornare i conti)

$$
\frac{d}{dt} \frac{\partial}{\partial \dot{q}^k}
(\sum\_{i=1}^N \frac{1}{2} m\_i v\_i^2) -
\frac{\partial}{\partial q^k} (\sum\_{i=1}^N \frac{1}{2}m\_i v\_i^2) 
 =
Q\_k
\qquad \qquad \forall k \in {1, \dots, n} $$

La sommatoria tra parentesi non è altro che l&#39;energia cinetica totale del sistema
di particelle, che indichiamo che T. Usando questa notazione otteniamo la forma
finale delle **equazioni di Eulero-Lagrange** (notare che c&#39;è un equazione per
ogni coordinata o grado di libertà):

$$ \frac{d}{dt} \frac{\partial T}{\partial \dot{q}^k} -
\frac{\partial T}{\partial q^k} = Q\_k \qquad \forall k \in {1, \dots, n} $$

Questo sistema di equazioni è alla base della formulazione Lagrangiana della
meccanica. Inserendo l&#39;energia cinetica e i momenti lagrangiani delle forze
attive per un dato sistema fisico, si possono ricavare equazioni pure di moto.

Ricordo che le quantità T e \\(Q\_k\\) dipendono dal sistema di riferimento
scelto, anche se non lo ho indicato per non rendere le formule troppo confuse.
