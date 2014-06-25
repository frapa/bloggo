---
layout: post
categories: en programming python games
---

Some years ago I found [Amit Patel's blog page on polygonal map generation](http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/).
Since then, I've become a fan of polygonal maps, even though I never produced anything with them because I couldn't find a decent library to compute
the voronoi diagram LINK of a set of points in python. Some time back I realized that scipy LINK has a function for computing the voronoi diagram.

So I decided to give a try, and I'm trying to write a small game that uses a polygonal map to model the world. Polygonal maps have many advantages
and disadvantages:

PRO:

 * The structure of the world is much richer: each polygon has a different number of connections with his neighbours.
 * Some algorithms will run faster. For example pathfinding: you can have the same world with 1000 polygons instead of one million
   grid cells.
