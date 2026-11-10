nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
nota3 = float(input('Informe a nota 3: '))
nota4 = float(input('Informe a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f'Aprovado, media {media}')

elif media >= 5:
    print(f'Recuperação, media {media}')

else:
    print(f'Reprovado, media {media}')

