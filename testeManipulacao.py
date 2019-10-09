'''
um string nao pode ser manipulado caractere a caractere
para isto,podemos criar um string vazio e concatenar caracter a caracter nele.
EXEMPLO:

'''
teste1=input('Digite um texto : ')
final=''
for i in range(len(teste1)-1,-1,-1):
    final=final+teste1[i].upper()
print(final)
