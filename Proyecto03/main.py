import datetime
from Grafo import *
x = datetime.datetime.now()
print(x)

nodo_raiz=1
print('nodo_raiz: ',nodo_raiz)


#******************************************************************************
#grafoMalla - Pocos nodos
gfMalla = Grafo.grafoMalla(3,3,dirigido=False)
gfMalla.display()
gfMalla.graphvizWithLabels()

dijkstra=gfMalla.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()


#grafoMalla - Muchos nodos
gfMalla = Grafo.grafoMalla(25,4,dirigido=False)
gfMalla.display()
gfMalla.graphvizWithLabels()

dijkstra=gfMalla.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()


#******************************************************************************
#grafoErdosRenyi - Pocos nodos
gfErdosReny = Grafo.grafoErdosRenyi(n=20, m=30, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphvizWithLabels()

dijkstra=gfErdosReny.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()

#grafoErdosRenyi - Muchos nodos
gfErdosReny = Grafo.grafoErdosRenyi(n=100, m=100, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphvizWithLabels()

dijkstra=gfErdosReny.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()



#******************************************************************************
#grafoGilbert - 30 nodos
gfGilbert = Grafo.grafoGilbert(n=30, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphvizWithLabels()

dijkstra=gfGilbert.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()


#grafoGilbert - 100 nodos
gfGilbert = Grafo.grafoGilbert(n=100, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphvizWithLabels()


dijkstra=gfGilbert.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()

#******************************************************************************
#grafoGeografico - 30 nodos
gfGeografico = Grafo.grafoGeografico(n=30, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphvizWithLabels()

dijkstra=gfGeografico.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()


#grafoGeografico - 100 nodos
gfGeografico = Grafo.grafoGeografico(n=100, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphvizWithLabels()

dijkstra=gfGeografico.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()

#******************************************************************************
#grafoBarabasiAlbert - 30 nodos
gfBarabasiAlbert = Grafo.grafoBarabasiAlbert(n=30, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphvizWithLabels()

dijkstra=gfBarabasiAlbert.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()


#grafoBarabasiAlbert - 100 nodos
gfBarabasiAlbert = Grafo.grafoBarabasiAlbert(n=100, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphvizWithLabels()

dijkstra=gfBarabasiAlbert.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()


#******************************************************************************
#grafoBarabasiAlbert - 30 nodos
gfDorogovtsevMendes = Grafo.grafoDorogovtsevMendes(30,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphvizWithLabels()

dijkstra=gfDorogovtsevMendes.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()

#grafoBarabasiAlbert - 100 nodos
gfDorogovtsevMendes = Grafo.grafoDorogovtsevMendes(100,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphvizWithLabels()

dijkstra=gfDorogovtsevMendes.Dijkstra(nodo_raiz)
dijkstra.display()
dijkstra.graphvizWithLabels()