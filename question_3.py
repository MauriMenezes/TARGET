'''
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
	• O menor valor de faturamento ocorrido em um dia do mês;
	• O maior valor de faturamento ocorrido em um dia do mês;
	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
IMPORTANTE:
	a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
	b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import json

with open('dados.json') as target_json:
    dados = json.load(target_json)

maior_valor = 0
menor_valor = 0

sum = 0
for i in dados:
    if (i['valor']) > maior_valor:
        maior_valor = i['valor']
    elif (i['valor'] < menor_valor):
        menor_valor = i['valor']

    sum += i['valor']
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')


# CALC MÉDIA
media = f'{ (sum/30):.4f}'
qtd_dia = 0
for i in dados:
    if i['valor'] > float(media):
        qtd_dia += 1

print(f'Quantidade de dias que ficou acima da média: {qtd_dia}')
