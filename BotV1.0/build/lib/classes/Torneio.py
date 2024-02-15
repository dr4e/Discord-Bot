import random
import math

def repeat_c(caractere, qtde):
    #fiz isso pra usar como uma função pra usar específicamente pra texto, pra outros fiz é só
    #tirar aql return '' e colocar um return None
    if(qtde < 0):
        raise ValueError("repeat method not accept negative numbers")

    if(qtde == 0):
        return ''

    if(qtde > 1):
        return(caractere + repeat_c(caractere, qtde -1))
    else:
        return(caractere)

class Torneio:
    def __init__(self, participantes):
        self.participantes = participantes[:]

    def chaveamento(self):
        chaves = []
        while(self.participantes):
            chaves.append(self.participantes.pop(random.randint(0, len(self.participantes) - 1)))

        txt = "```\n"
       
        for i in range(0, len(chaves), 2):

            tamanho = max(len(chaves[i]), len(chaves[i+1]))

            espacos = ((tamanho - len(chaves[i])) // 2)
            extra = ''
            if(len(chaves[i]) < tamanho and ((len(chaves[i]) % 2 and (not len(chaves[i+1]) % 2)) or (len(chaves[i+1]) % 2 and (not len(chaves[i]) % 2)))):
                extra = ' '
            
            txt += repeat_c("-", tamanho + 4) + "\n|" + repeat_c(' ', espacos) + f" {chaves[i]} " + repeat_c(' ', espacos) + extra + "|\n"  + repeat_c("-", tamanho + 4)
            
            espacos = (tamanho - len(chaves[i+1])) // 2
            extra = ''

            if(len(chaves[i+1]) < tamanho and ((len(chaves[i]) % 2 and (not len(chaves[i+1]) % 2)) or (len(chaves[i+1]) % 2 and (not len(chaves[i]) % 2)))):
                extra = ' '

            txt += "\n|" + repeat_c(' ', espacos) + f" {chaves[i+1]} " + repeat_c(' ', espacos) + extra + "|\n"  + repeat_c("-", tamanho + 4) + "\n"

        txt += "```\n"    
        return txt