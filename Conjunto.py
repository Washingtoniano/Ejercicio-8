from Numero import num
class conjunto():
    __indice=[]
    def __init__(self):
        self.__indice=[]
    def __add__(self, other):
        nuevo=self.__indice+other.__indice
        for i in range (len(self.__indice)):
            band=True
            for j in range (len (other.__indice)):
                if (self.__indice[i]==other.__indice[j]):
                    mo=int(self.__indice[i])
                    nuevo.remove(mo)
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
        mo=None
        nuevo=[]
        for i in range (len(self.__indice)):
            band =False
            for j in range (len (other.__indice)):
                if (self.__indice[i]!=other.__indice[j]):
                    band=True
                else:
                    mo=self.__indice[i]
            if (band==True):
                nuevo.append(self.__indice[i])
        nuevo.remove(mo)
        return (nuevo)
    def agregar (self,va):
        self.__indice.append(va)
    def __str__(self):
        return("Valores:{}".format(self.__indice))
