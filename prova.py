def cambiarClavesDic( dic, list ):

    num = 0

    for i in dic:
        print(dic[i])
        dic[list(num)] = dic[i].pop()
        num += 1


dic = { 'usuario1': 23, 'usuario7': 10, 'usuario2' : 4 }
nombres = ["Pepe", "alfonso", "ana", "pedro", "juan", "pepito", "Toni"]

print( dic )

cambiarClavesDic(dic, nombres)

print( dic )