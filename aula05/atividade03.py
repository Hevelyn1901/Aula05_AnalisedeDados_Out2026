valor_compra = float(input('Informe qual foi o valor da compra: '))
fidelidade = input('Programa de Fidelidade? [S/N] ').lower()[0]
frete = 25.00

if valor_compra > 200 or fidelidade == 's' :
    print(f'Sendo nosso melhor cliente, nesta compra você ganhou frete grátis. Sua compra ficou no valor de R$ {valor_compra:.2f}. Obrigada e volte sempre!')

else:
    valor_total = valor_compra + frete
    print(f'Sua compra ficou no valor de R$ {valor_compra:.2f} \nNosso frete custa R$ {frete} \nValor total da sua compra ficou em R$ {valor_total:.2f}')   
   