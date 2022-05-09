from Numero import num
class conjunto():
    __indice=[]
    def __init__(self):
        self.__indice=[]
    def __add__(self, other):
        self.__indice.sort()
        other.__indice.sort()
        nuevo=self.__indice
        for objeto in other.__indice:
            if objeto not in nuevo:
                nuevo.append(objeto)
        return (nuevo)
    def agregar (self,va):
        self.__indice.append(va)

    def __eq__(self, other):
        ban=False
        t=-1
        if (len (self.__indice)==len(other.__indice)):
            ban=True
        if (ban==True):
            self.__indice.sort()
            other.__indice.sort()
            for i in range (len (self.__indice)):
                if self.__indice[i]==other.__indice[i]:
                    t=1
                else:
                    t=-1
        if t==1 and ban==True:
            return ("Los conjuntos  son iguales")
        else:
            return ("Los conjuntos no son iguales")
    def __sub__(self, other):
        self.__indice.sort()
        other.__indice.sort()
        mo=None
        nuevo=[]
        for objeto in self.__indice:
            if objeto not in other.__indice:
                nuevo.append(objeto)
        return (nuevo)
    def agregar (self,va):
        self.__indice.append(va)
    def __str__(self):
        return("Valores:{}".format(self.__indice))
