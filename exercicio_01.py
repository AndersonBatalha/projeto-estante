# coding: utf-8

def media_final_aprovado_reprovado(prova1,prova2,exercicios_programacao1,
    exercicios_programacao2):
    ''' Recebe as notas das 2 provas e 2 exercícios de programação e retorna 
    se o aluno foi ou não aprovado. As provas tem peso 7 e os exercícios 
    tem peso 3. Cada parcial tem peso igual.'''
    parcial1 = (prova1 * 0.7 + exercicios_programacao1 * 0.3)
    parcial2 = (prova2 * 0.7 + exercicios_programacao2 * 0.3)
    soma = parcial1 + parcial2
    if soma < 7:
        return False
    else:
        return True



def testa_lados(a,b,c):
    ''' Receba os três lados de um triângulo. Informe se os valores 
    podem ser um triângulo. Indique, caso os lados formem um triângulo, 
    se o mesmo é: equilátero, isósceles ou escaleno. '''
    if a > b + c or b > a + c or c > a + b:
        return ("Não forma um triângulo")
    else:
        if a == b == c:
            return ("Triângulo equilátero")
        elif a != b != c:
            return ("Triângulo escaleno")
        elif a != b == c or a == b != c:
            return ("Triângulo isósceles")

def data_valida(data):
    '''Valida data'''
    dia = int(data.split("/")[0])
    mes = int(data.split("/")[1])
    ano = int(data.split("/")[2])
    if ano >= 1:
        if (mes >= 1 and mes <= 12):
            if mes == 2 and ano_bissexto(ano) == True:
                if dia >= 1 and dia <= 29:
                    return True
                else:
                    return False
            elif mes == 2 and ano_bissexto(ano) == False:
                if dia >= 1 and dia <= 28:
                    return True
                else:
                    return False
            else:
                if mes in [1,3,5,7,8,10,12]:
                    if dia >= 1 and dia <= 31:
                        return True
                    else:
                        return False
                else:
                    if dia >= 1 and dia <= 30:
                        return True
                    else:
                        return False
        else:
            return False
    else:
        return False    


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def ano_bissexto(ano):
    ''' Determine se um ano é bissexto'''
    if ano%4 == 0:
        if ano%100 == 0:
            if ano%400 == 0:
                eb = True
            else:
                eb = False
        else:
            eb = True
    else:
        eb = False
    return eb

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = ' Falhou.'
    else:
        prefixo = ' Passou.'
        acertos += 1
    print ('%s Esperado: %s \tObtido: %s' % (prefixo, repr(esperado), 
        repr(obtido)))

def main():

    print('Média final:')
    test(media_final_aprovado_reprovado(10,10,0,0), True)
    test(media_final_aprovado_reprovado(0,0,10,10), False)
    test(media_final_aprovado_reprovado(10,10,10,10), True)
    test(media_final_aprovado_reprovado(0,0,5,0), False)

    print('Triângulos:')
    test(testa_lados(7,1,2),'Não forma um triângulo')
    test(testa_lados(7,2,1),'Não forma um triângulo')
    test(testa_lados(1,7,2),'Não forma um triângulo')
    test(testa_lados(1,2,7),'Não forma um triângulo')
    test(testa_lados(2,1,7),'Não forma um triângulo')
    test(testa_lados(2,7,1),'Não forma um triângulo')
    test(testa_lados(2,2,2),'Triângulo equilátero')
    test(testa_lados(3,3,3),'Triângulo equilátero')
    test(testa_lados(2,3,4),'Triângulo escaleno')
    test(testa_lados(2,4,3),'Triângulo escaleno')
    test(testa_lados(3,4,2),'Triângulo escaleno')
    test(testa_lados(3,2,4),'Triângulo escaleno')
    test(testa_lados(2,3,3),'Triângulo isósceles')
    test(testa_lados(3,2,2),'Triângulo isósceles')
    test(testa_lados(3,3,2),'Triângulo isósceles')

    print('Valida datas:')
    test(data_valida("01/01/2014"),True)
    test(data_valida("31/01/2014"),True)
    test(data_valida("00/00/0000"),False)
    test(data_valida("29/02/2014"),False)
    test(data_valida("29/02/2016"),True)
    test(data_valida("30/04/2014"),True)
    test(data_valida("31/04/2014"),False)  
    test(data_valida("30/06/2014"),True)
    test(data_valida("31/06/2014"),False) 
    test(data_valida("30/09/2014"),True)
    test(data_valida("31/09/2014"),False) 
    test(data_valida("30/11/2014"),True)
    test(data_valida("31/11/2014"),False)
    test(data_valida("32/01/2014"),False)
    test(data_valida("01/01/0000"),False)
    test(data_valida("01/13/2014"),False)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")