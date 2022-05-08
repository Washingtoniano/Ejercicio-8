class conjunto():
    __numeros=[]
    def init (self):
        self.__numeros=[]
    def __add__(self, other):
        nuevo=[]
        new=None
        nuevo.append(self.__numeros+other.__numeros)
        for i in range (len(nuevo)):
            for j in range (len(nuevo)):
                if nuevo[i]==nuevo[j]:
                    new=int(nuevo[i])
                    nuevo.remove(new)
        return (nuevo)
    def agregar (self,va):
        self.__numeros.append(va)

    def __eq__(self, other):
        ban=False
        t=-1
        if (len (self.__numeros)==len(other.__numeros)):
            ban=True
        if (ban==True):
            self.__numeros.sort()
            other.__numeros.sort()
            for i in range (len (self.__numeros)):
                if self.__numeros[i]==other.__numeros[i]:
                    t=1
                else:
                    t=-1
        if t==-1 or ban==False:
            return ("Los conjuntos  no son iguales")
        else:
            return ("Los conjuntos son iguales")
    def __sub__(self, other):
        band=False
        nuevo=[]
        for i in range (len(self.__numeros)):
            for j in range (len (other.__numeros)):
                if (self.__numeros[i]!=other.__numeros[j]):
                    band=True
                else:
                    band=False
            if band==True:
                va=int(self.__numeros[i])
                nuevo.append(va)
        return (nuevo)



