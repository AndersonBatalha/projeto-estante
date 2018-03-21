# coding: utf-8

def troca_caixa(texto):
    '''Vogais ficam em caixa alta (maiúsculas)
    Consoantes ficam em caixa baixa (minúsculas)'''
    novo_texto = ""
    for caracter in texto:
        if caracter.isupper() == True:
            novo_texto += caracter.lower()
        else:
            novo_texto += caracter.upper()
    return novo_texto

def altera_salarios(salarios):
    '''Recebe uma lista de salários e devolva uma lista com os salários
    alterados.
    Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5% 
    Salário mínimo para referência: R$ 724,00
    '''
    salario_minimo = 724
    for salario in salarios:
        if salario <= salario_minimo:
            salarios[salarios.index(salario)] = salario + (salario * 0.2)
        elif salario > salario_minimo and salario <= 2 * salario_minimo:
            salarios[salarios.index(salario)] = salario + (salario * 0.15)
        elif salario > 2 * salario_minimo and salario <= 5 * salario_minimo:
            salarios[salarios.index(salario)] = salario + (salario * 0.10)
        elif salario > 5 * salario_minimo:
            salarios[salarios.index(salario)] = salario + (salario * 0.05)
    return salarios



def intercalamento_listas(lista1,lista2):
    ''' Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo
    intercalamento entre as duas.'''
    lista = lista1 + lista2
    lista.sort()
    return lista

def conta_letras(texto):
    '''Receba uma string e devolva um dicionário onde a chave seja uma letra e seu 
    valor correspondente seja a quantidade de vezes que esta letra aparece na string, 
    independente de caixa (maiúscula ou minúscula)'''
    string = texto.lower()
    quantidade_letras = {}
    for caracter in string:
        quantidade_letras[caracter] = string.count(caracter)
    return quantidade_letras

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

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

    print('     \nTroca caixa:')
    test(troca_caixa("aRaQuaRi"), "ArAqUArI") # normal
    test(troca_caixa("CaXiaS Do SuL"), "cAxIAs dO sUl") # com espaços

    print('     \nAumenta salários:')
    test(altera_salarios([500,724.0,725.00,1448.00,1449.00,3620.00,3621.00,4000.00]), 
        [600.0, 868.8, 833.75, 1665.2, 1593.9, 3982.0, 3802.05, 4200.0])

    print('     \nLista Intercalada:')
    test(intercalamento_listas([1,3,5,7,9],[2,4,6,8,10]), [1,2,3,4,5,6,7,8,9,10])

    print('     \nconta letras')
    test(conta_letras("a"), {'a': 1})
    test(conta_letras("ana"), {'a': 2, 'n':1})
    test(conta_letras("bala"),  {'a': 2, 'b': 1, 'l': 1})
    test(conta_letras("bota"), {'a': 1, 'b': 1, 't': 1, 'o': 1})
    test(conta_letras("banana"), {'a': 3, 'b': 1, 'n': 2})
    test(conta_letras("abacaxi"), {'a': 3, 'x': 1, 'c': 1, 'b': 1, 'i': 1})
    test(conta_letras("araquari"), {'a': 3, 'q': 1, 'r': 2, 'u': 1, 'i': 1})
    test(conta_letras("Instituto Federal Catarinense"),  {'a': 3, ' ': 2, 'c': 1, 'e': 4, 'd': 1, 'f': 1, 'i': 3, 'l': 1, 'o': 1, 'n': 3, 's': 2, 'r': 2, 'u': 1, 't': 4})


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")