'''
int INDICE = 13, SOMA = 0, K = 0;
	enquanto K < INDICE faça
	{
		K = K + 1;
		SOMA = SOMA + K;
	}
	imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
'''


i = 13
sum = 0
k = 0

while k < i:
    k += 1
    sum += k
print(f'O valor da soma é: {sum}')
