from claseConjunto import Conjunto
if __name__=="__main__":
    unNuevoConjunto=Conjunto()
    print("Inicializar conjunto uno")
    unNuevoConjunto.inicializar()
    print("conjunto {}".format(unNuevoConjunto))
    otroConnjunto=Conjunto()
    print("Inicializar conjunto dos")
    otroConnjunto.inicializar()
    opcion=0
    while opcion!=4:
       print("__MENU__")
       print("1-Sumar conjuntos \n2-Restar conjuntos \n3- Comparar conjuntos \n4- Salir menu")
       opcion=int(input("Ingrese la opcion que desea realizar"))
       if opcion==1:
           unNuevoConjunto+otroConnjunto
       if opcion==2:
            unNuevoConjunto-otroConnjunto

       if opcion==3:
            unNuevoConjunto==otroConnjunto


