valor_lanche = float(input('Informe o valor do lanche: '))
distancia = float(input('Informe a distância: '))
frete = 8

if valor_lanche > 50 and distancia <= 3:
    valor_final = valor_lanche
    print('Parabéns! Seu pedido vai chegar de graça para você.')

else:
    valor_final = valor_lanche + frete 
    print(f'Frete de R$ {frete} \nValor final ficou em R$ {valor_final:.2f}')   