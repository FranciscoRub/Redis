import redis
keyslang="Slang"
keysig="Significado"
r= redis.Redis(host='127.0.0.1',port=6379)
r.set("id",-1)
print(r.keys())



def Añadir(Slang,Significado):
    r.incr("id")
    r.rpush(keyslang, Slang)
    r.rpush(keysig, Significado)
    print("\n Se agregó el slang con éxito")

#Slangant = slang anterior, Slangact= slang actual
def editarregistro(SlangAnt,newSlang,newSignificado):
    CantSlang = r.llen(keyslang)
    for i in range(CantSlang):
        Slangact = r.lindex(kesyslang, i).decode('utf-8')
        if(Slangact == SlangAnt):
            r.lset(keyslang, i, NewSlang)
            r.lset(keysig, i, NewSignificado)
            break
    print("El slang"+SlangAnt+"ha sido editado")

def verregistros():
    CantSlang = r.llen(keyslang)
    for i in range(CantSlang):
        print(f'{i + 1}. Slang: {r.lindex(keyslang, i).decode("utf-8")} \n Significado: {r.lindex(keysig, i).decode("utf-8")}')

def revisar(Slang):
    Cantslang=r.llen(keyslang)
    slangexist=False
    for i in range(Cantslang):
        Slangact = r.lindex(keyslang, i).decode('utf-8')
        if(Slangact == Slang):
            slangexist = True
            break
    return slangexist

def eliminarregistro(Slang):
    CantSlang = r.llen(keyslang)
    for i in range(CantSlang):
        Slangact = r.lindex(keyslang, i).decode('utf-8')
        significadoact = r.lindex(keysig, i).decode('utf-8')
        if(keyslang == Slang):
            r.lrem(keysalng, i, Slangact)
            r.lrem(keysig, i, significadoact)
            break
    print("\n Slang eliminado")


print("--------------------------Diccionario de Slang Panameño-------------------------")
menuprincipal = int(input("--Menú Principal: \n 1- agregar nueva palabra \n 2- Editar palabra existente\n 3- Eliminar palabra existente \n 4- Ver listado de palabras \n 5- Buscar significado de palabra \n 6- Salir \n Elija una opción: "))


while menuprincipal !=6:
    if menuprincipal == 1:
        islang = input("\nIngrese slang:\n")
        isignificado = input(
            "\nIngrese significado: \n")
        if(len(islang) and len(isignificado)):
            if(revisar(islang)):
                print("\nSlang ya registrado, introduzca otro:")
            else:
                Añadir(islang, isignificado)
        else:
            print("/n Agregue datos por favor")
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 2:
        islang = input("\nSlang a editar: \n")

        nuevoslang = input("\nNuevo slang:\n")

        nuevosignificado  = input("\nSignificado: \n")

        if(len(nuevoslang) and len(nuevosignificado) and len(islang)):
            if(revisar(islang)):
                editarregistro(islang, nuevoslang, nuevosignificado)
            else:
                print("\nEsta palabra no se encuentra en el diccionario")

        else:
            print("/n Agregue datos por favor")
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 3:
        islang= input("\nSlang a borrar: ")
        if(len(islang)):
            if(revisar(islang)):
                eliminarregistro(islang)

            else:
                print("\nEsta slang no se encuentra en el diccionario")

        else:
             print("/n Agregue datos por favor")
        menuprincipal==input("preciones Enter para seguir: ")
        
    elif menuprincipal ==4:
        verregistros()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==5:
        islang = input("\n slang que desea conocer significado:\n")
        if(len(islang)):
            if(revisar(islang)):
                CantSlang = r.llen(keyslang)
                for i in range(CantSlang):
                    slangact = r.lindex(keyslang, i).decode('utf-8')
                    if(slangact == islang):
                        print(
                            f'La definicion es: {r.lindex(DefinicionClave, i).decode("utf-8")}')
                        break

            else:
                print("\nSlang no se encuentra en diccionario")

        else:
            print("/n Agregue datos por favor")
        menuprincipal==input("preciones Enter para seguir: ")
    else:
        print("Por favor digite una opción válida")
        
    menuprincipal = int(input("\n\n\nMenú Principal: \n 1- agregar nueva palabra \n 2- Editar palabra existente \n 3- Eliminar palabra existente \n 4- Ver listado de palabras \n 5- Buscar significado de palabra \n 6- Salir \n"))


    
