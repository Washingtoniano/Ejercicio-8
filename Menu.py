from Numero import num
from Conjunto import conjunto

class menu():
    __con=None
    def __init__(self):
        self.__con=conjunto()
    def inicial(self):
        prim=conjunto()
        segun=conjunto()
        va= (input("Ingrese los valores del primer conjunto(para finalizar ingrese 'a')\n"))
        while (va!='a'):
            prim.agregar(va)
            va=input()
        va= (input("Ingrese los valores del segundo conjunto(para finalizar ingrese 'a')\n"))
        while (va!='a'):
            segun.agregar(va)
            va=input()

        op= int(input ("Seleccione la opcion que desea ejecutar\n\t 1.Sumar conjuntos\t2.Restar conjuntos\t3.Comparar Conjuntos"))
        while op!=4:
            self.operador(op,segun,prim)
            op= int(input ("Seleccione la opcion que desea ejecutar\n\t 1.Sumar conjuntos\t2.Restar conjuntos\t3.Comparar Conjuntos"))
        print ("adios")
    def operador (self,op,segun,prim):
        if op==1:
            self.opcion1(segun,prim)
        elif op==2:
            self.opcion2(segun,prim)
        elif (op==3):
            self.opcion3(segun,prim)
        elif (op!=4):
            print ("Error")
    def opcion1(self,segun,prim):
        print (prim+segun)
    def opcion2(self,segun,prim):
        print (prim-segun)
    def opcion3(self,segun,prim):
        print (prim==segun)
