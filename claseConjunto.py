import copy
class Conjunto:
    __numeros=[]
    def __init__(self):
        self.__numeros=[]


    def inicializar(self):
        opcion="si"
        while(opcion=="si"):
            numero=input("Ingrese un numero para agregar al conjunto")
            self.__numeros.append(numero)
            opcion=input("¿desea seguir agrgando numero?\nEscriba  si para seguir agregandoo no en caso contrario")


    def __str__(self):
        s=""
        for num in self.__numeros:
            s+=num+","

        return s
    
    def RetornarDatos(self):
        return self.__numeros
    

    def __add__(self,otroConjunto):
        nuevo=self.__numeros.copy()

        for i in range (len(otroConjunto.RetornarDatos())):
            j=0
            while(j<len(self.__numeros)) and (self.__numeros[j]!=otroConjunto.RetornarDatos()[i]):
                j+=1
            if j>len(self.__numeros):
                nuevo.append(otroConjunto.RetornarDatos()[i])
        print("union {}".format(nuevo))


    def __sub__ (self,otroConjunto):
        nuevo=self.__numeros.copy()

        for i in range (len(otroConjunto.RetornarDatos())):
            j=0
            while(j<len(self.__numeros)) and (self.__numeros[j]!=otroConjunto.RetornarDatos()[i]):
                j+=1
            if j>len(self.__numeros):
                nuevo.pop(j)
        print("diferencia {}".format(nuevo))


    def __eq__(self, o):
        if len(self.__numeros)!=len(o.RetornarDatos()):
            print("Los conjuntos son distintos")
        else:
            i=0
            band=True
            while (i<len(o.RetornarDatos()))and (band==True):
                j=0
                while (i<(len(o.RetornarDatos())))and (self.__numeros[j]!=o.RetornarDatos()[i]):
                    j+=1
                if j>=len(o.RetornarDatos()):
                    print("Los conjuntos no son iguales")
                    band=False
                else:
                    i+=1
            if band==True:
                print("Los conjuntos son iguales")
        
            
        