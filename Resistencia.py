class Vertice:
    """
    Es la clase vertice que utliza el grafo
    """

    def __init__(self,clave):
        """
        Es el constructor de la clase almacena la info del vertice
        """
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self, vecino, peso=0):
        """
        Agrega una referencia a otros vertices
        """
        self.conectadoA[vecino] = peso

    def __str__(self):
        """
        :return: Retorna un str con las conecciones del vertice
        """
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        """

        :return: Retorna una lista de todos los vertices conectados
        """
        return self.conectadoA.keys()

    def obtenerId(self):
        """

        :rtype: Retorna el id del vertice
        """
        return self.id

    def obtenerpeso(self,vecino):
        """
        :param vecino: vertice conectado
        :return: retorna el peso
        """
        return self.conectadoA[vecino]

class Grafo:
    """
    Es la clase que almacena los vertices y los pesos de la simulacion
    """
    def __init__(self):
        """
        Es el constructor de la clase almacena la informacion del grafo
        """
        self.listaVertices = {}
        self.numVertices = 0
        self.elementos = []

    def agregarVertice(self, clave):
        """
        :param clave: El valor del nuevo vertice
        :return: el nuevo vertice
        """
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        """
        :param n: El valor del vertice
        :return: Retorna el vertice si existe
        """
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self, n):
        """
        Revisa si contiene ese vertice
        :return:   El valor booleano
        """
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        """
        :param de: de donde parte
        :param a: al vertice que llega
        :param costo: el peso de la arista
        :return: None
        """

        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        """
        :return: Una lista de los vertices del gradfo
        """
        return self.listaVertices.keys()

    def __iter__(self):
        """
        :return: Itera sobre la lista de valores
        """
        return iter(self.listaVertices.values())

    def agregarElement(self, nuevo):
        """
        Agrega un nuevo elemento al grafo
        :param nuevo:
        :return: Si pudo agregarse o no
        """
        if nuevo not in self.elementos:
            self.elementos.append(nuevo)
            return True
        else:
            return False
