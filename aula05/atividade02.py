nota_final = float(input('Informe a nota final: '))
frequencia = float(input('Informe a frequencia do aluno: '))
mensalidade = 300.00

if nota_final >= 7 and frequencia >= 75:
    desconto = mensalidade * 0.20
    print(f'Parabéns! Nossa mensalidade é no valor de R$ {mensalidade:.2f} \nE você ganhou um desonto de R$ {desconto:.2f} \nFicando no total de R$ {mensalidade - desconto:.2f}')

else:
    print(f'O valor da sua mensalidade será de R$ {mensalidade:.2f}. Sem descontos!')    
