def funcion(dic, lista):
    dic3={}
    for clave in dic:
        for i in lista:
           if i==clave:
               dic3[clave]=dic[i]
               print(dic3)

dic = {"first": 20, "ana": 556, "third": 212, "fourth": 89}
nombres = ["Pepe", "ana", "juan", "Toni"]
funcion(dic,nombres)



def dicNumToMin(dic):
    return min(dic.values())


# ----------- MAIN -----------

dic = {"first": 20, "second": 556, "third": 212, "fourth": 89}

print( dicNumToMin(dic) )


