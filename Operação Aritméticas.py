# Operações aritméticas

nome= input('Qual é seu nome?')
print('Prazer em te conhecer{:=^20}!'.format(nome))
n1= int(input('Um valor x: '))
n2= int(input('Outro valor: '))
s= n1+n2
m= n1*n2
d= n1/n2
di= n1//n2
e= n1**n2

print('A soma é {} \n O produto é {} \n Divisão é {:.3f}' .format(s, m, d), end=' ')
print('\n Divisão inteira {} \n Potência {}'.format(di, e))
