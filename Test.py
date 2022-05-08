from Conjunto import conjunto

def test():
    unconjunto=conjunto()
    otroconjunto=conjunto()
    unconjunto=[1,2,3]
    otroconjunto=[3,4,5]
    print ("Conjunto 1={}".format(unconjunto))
    print ("Conjunto 2={}".format(otroconjunto))
    print ("opcion 1")
    print (unconjunto+otroconjunto)
    print ("Opcion2")
    print (unconjunto-otroconjunto)
    print ("Opcion3")
    if (unconjunto==otroconjunto)==False:
        print ("Los conjuntos no son iguales")
    else:
        print ("Los conjuntos son iguales")

