lista1 = []
lista2 = []

def somalista(lista1,lista2):
    somalista = []
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            soma = lista1[i] + lista2[i]
            if soma > 9:
                soma = soma%10
                somalista.insert(i, soma)
                somalista[i-1] += 1
            else:
                somalista.append(soma)
            print(somalista)
    else: 
        if len(lista1)>len(lista2):
            while len(lista1)>len(lista2):
                lista2.insert(0,0)
                for i in range(len(lista1)):
                      soma = lista1[i] + lista2[i]
                      if soma > 9:
                          soma = soma%10
                          somalista.insert(i, soma)
                          somalista[i-1] += 1
                      else:
                          somalista.append(soma)
                      print(somalista)
        else:
            while len(lista1)<len(lista2):
                lista1.insert(0,0)
                for i in range(len(lista1)):
                    soma = lista1[i] + lista2[i]
                    if soma > 9:
                        soma = soma%10
                        somalista.insert(i, soma)
                        somalista[i-1] += 1
                    else:
                        somalista.append(soma)
                    print(somalista)
    return" "
print(somalista(lista1,lista2))