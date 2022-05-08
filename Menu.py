from Conjunto import conjunto
class menu():
    __con=conjunto()
    def __init__(self):
        self.__con=conjunto()
    def inicial(self):
        prim=conjunto()
        segun=conjunto()
        va= (input("Ingrese los valores del primero conjunto(para finalizar ingrese un valor que no sea entero)\n"))
        while (va!=str or va!=float):
            prim.agregar(va)
        va= (input("Ingrese los valores del segundo conjunto(para finalizar ingrese un valor que no sea entero)\n"))
        while (va!=str or va!=float):
            segun.agregar(va)

    def operador (self):
        op= int(input ("Seleccione la opcion que desea ejecutar\n\t 1.Sumar conjuntos\t2.Restar conjuntos\t3.Comparar Conjuntos"))
        if op==1:
            self.opcion1()
        elif op==2:
            self.opcion2()
    #def opcion1(self):

    #def opcion2(self):
    #def opcion3(self):
