def mode(lista_numeros):
    if len(lista_numeros) != 0:
        largo_lista_de_numeros = len(lista_numeros) 
        aux = [0]*largo_lista_de_numeros
        lista_numeros.sort()                                             
        n = 0                                              
        for i in range(0, largo_lista_de_numeros):       
           if lista_numeros[i] == lista_numeros[n]:
             aux[n]=aux[n]+1
           else:
              n = i
              aux[n] = aux[n] +1
        max = aux[0]
        for i in aux:
           if max < i:
              max = i
        modas = []
        largo_aux = len(aux)
        for j in range(0, largo_aux):
           if aux[j]==max:
               modas.append(lista_numeros[j])
        del aux
        return modas