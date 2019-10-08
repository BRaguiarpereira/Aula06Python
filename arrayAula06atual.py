'''
Array (VetoresEmatrizes)
Um vetor(array) é um conjunto ordenado de variaveis de um mesmo tipo.

Definimos:

-tipo do dado
-nome
-tamanho(da celula)

obs: cada celula e numerada,começando em 0 indo até tamanho-1

Vetores sao normalmente usados com comandos de repetiçao (for ou while)

No Python , nao há vetores,e sim listas.Porem o tipo string se comporta como vetor

EXEMPLO:

'''

'''
texto = 'Python'
for i in range(0,6):
    print(texto[i])
'''
    
'''
len(string1): devolve o tamanho de um string ou uma lista
'''

'''
teste = input('Digite algo :')
print('{} caracteres'.format(len(teste)))
'''

'''
Operaçoes com strings
+: concotena 2 strings
teste1 = 'CC'
teste2 = 'SI'
print(teste1+teste2)
print(teste2+teste1)

N*str1{

str1+str1+str1+str1+str1+str1

}
'''

'''
teste1='teste'
teste2='python'
print(teste1+teste2)
print(2*(teste1+teste2))
print('primeira string : {} caracteres'.format(len(teste1)))
print('segunda string : {} caracteres'.format(len(teste2)))
'''

'''
Outros metodos para manipular strings

-string.replace('palavra1','palavra2')

só executa se os dois forem uma palavra


-string.count('x')

conta quantas vezes x aparece no string

-string.find('x')

indica a posiçao em que x aparece vetoriamente

-string.upper('x')

transforma o string em letra maiuscula
'''

teste1='Frase para testar os metodos'
print(teste1.replace('testar','coisar'))
print('A letra a aparece {} vezes'.format(teste1.count('a')))
print('A letra x aparece {} vezes'.format(teste1.count('x')))
print(teste1.split())
print(teste1.upper())
print(teste1.lower())



























