# IFPB - Campina Grande
# Lempel-Ziv-Welch-Binario
# Aluno: Judenilson Araujo
# Professor: Jeronimo Silva Rocha

from dataclasses import replace

def codificador(seq):
    dicionario = {0:["0","*"], 1:["0","0"], 2:["0","1"]}
    ene="0"
    transmitir = []
    m = 3
    flag = False
    seq += '*'

    for a in seq:
        for i in dicionario:
            if dicionario[i] == [ene,a]:
                ene = str(i)
                flag = True
                break
        if flag == False:
            transmitir.append(ene)
            dicionario[m] = [ene,a]
            m += 1
            for i in dicionario:
                if dicionario[i] == ["0",a]:
                    ene = str(i)
                    break
        flag = False

    return transmitir

def decodificador(seq):
    dicionario = {0:["0","*"], 1:["0","0"], 2:["0","1"]}
    bes = {}
    m = 3
    n=""
    a=""
    transmitir = []
    
    for r in seq:
        t = []
        bm = "b"
        bm += str(m)
        dicionario[m]=[r,bm]

        while(1):
            n = dicionario[int(r)][0]   
            a = dicionario[int(r)][1]
            t.insert(0, a)
            if n != "0":
                r = n
            else:
                if ((m-1)>2):
                    dicionario[m-1][1] = a
                    bes["b" + str(m-1)] = a
                m = m + 1
                break
        for i in range(len(t)):
            if (t[i]) in bes:
                t[i] = bes[t[i]]
            transmitir.append(t[i])

    return transmitir

print(codificador("00000001"))
print(decodificador("13412"))