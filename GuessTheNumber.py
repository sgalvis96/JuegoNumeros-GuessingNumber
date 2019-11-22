import random
class guess:
####################################################
    def dificultad(d):
        try:
            if d == "facil":
                a = 30
            if d == "medio":    #SELECCION DIFICULTAD
                a = 60
            if d == "dificil":
                a = 90
        except TypeError:
            print ("No valido")
        return a        #RETORNO DIFICULTAD (30/90/60)
#####################################################
    def adivine(limite):
        usuario = 0         #NUMERO A INGRESAR EL USUARIO
        for i in range(1):  #FOR PARA OBTENER EL NUMERO RANDOM
            aleatorio = random.randint(0, limite) #VARIABLE QUE ALMACENARÁ EL NUMERO (DE 0 A DIFICULTAD)
        while usuario != aleatorio: #CONDICION DEL WHILE
            usuario = int(input("Ingrese el numero que cree que es: ")) #ENTRADA DEL USUARIO
            if usuario < aleatorio:     #CONDICION PARA INFORMAR INFERIORIEDAD
                print("Mas para arriba")
            else:                       #CONDICION PARA INFORMAR SUPERIORIDAD
                print("Mas para abajo")
#####################################################
    nivel = input("Seleccione dificultad: ")
    limit = dificultad(nivel)   #LLAMADA DEL METODO LIMITE
    adivine(limit)              #LLAMADA DEL METODO DE ADIVINAR
    print("Felicidades!")       #CHAO


