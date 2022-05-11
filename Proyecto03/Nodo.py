#Clase Nodo
class Nodo:
  def __init__(self, id):
    self.id = id
    self.grado=0

    #Parametros algoritmo de dijkstra
    self.padre=None
    self.visitado=False
    self.distancia=float('inf')

  def __str__(self):
      return str(self.id)
  def __eq__(self, otroNodo):
      return self.id == otroNodo.id
  def __lt__(self, otroNodo):
      return self.distancia < otroNodo.distancia


#******************************************************************************
