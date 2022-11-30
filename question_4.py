'''
 Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

	SP – R$67.836,43
	RJ – R$36.678,66
	MG – R$29.229,88
	ES – R$27.165,48
	Outros – R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
'''
sp = 20.2032
rj = 36.67866
mg = 29.22988
es = 27.16548
outros = 19.84953

estados = ['sao paulo', 'Rio de janeiro',
           'Minas Gerais', 'Espirito Santo', 'Outros']

fat = [sp, rj, mg, es, outros]
total = sum(fat)

c = 0
for i in fat:
    percent = (i/total)*100
    print(f'O percentual de {estados[c]} é {percent:.2f}%')
    c += 1
