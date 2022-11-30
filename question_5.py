'''
Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
	b) Evite usar funções prontas, como, por exemplo, reverse;
'''

frase_1 = 'inverter esse texto'
frase_2 = 'Maurilio Souza Menezes'


def inverter(text):
    return text[::-1]


print(inverter(frase_1))
print(inverter(frase_2))
