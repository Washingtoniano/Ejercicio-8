from Numero import num
from Conjunto import conjunto

def test():
    conjunto1=conjunto()
    conjunto1.agregar(1)
    conjunto1.agregar(2)
    conjunto1.agregar(3)

    conjunto2=conjunto()
    conjunto2.agregar(3)
    conjunto2.agregar(4)
    conjunto2.agregar(5)
    print ("Conjunto 1={}".format(conjunto1))
    print ("Conjunto 2={}".format(conjunto2))
    print ("opcion 1")
    print (conjunto1 + conjunto2)
    print ("Opcion2")
    print (conjunto1 - conjunto2)
    print ("Opcion3")
    print (conjunto1==conjunto2)

