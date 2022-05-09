class num():
    __numeros=int
    def init (self,numero):
        self.__numeros=numero
    def __add__(self, other):
        nuevo=[]
        band=False
        for i in range (len(self.__numeros)):
            for j in range(len (other.__numeros)):
               if self.__numeros[i]==other.__numeros[j]:
                    band =True
            if(band!=True):
                nuevo.append(self.__numeros[i])

        return (nuevo)
    def valor(self):
        return self.__numeros



