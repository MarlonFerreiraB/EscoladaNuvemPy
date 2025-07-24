

list_notas = []
while True:
    nota = input('Digite a nota (ou "sair" para encerrar): ')
    if nota == 'sair':
        media = sum(list_notas)/len(list_notas)
        print(f'A média das notas é: {media:.2f}')
        break
    try:
        nota_float = float(nota)
        if nota_float < 0 or nota_float > 10:
            print('Nota inválida digite novamente.')
            continue
        list_notas.append(nota_float)
    except ValueError:
        print('Entrada inválida digite um número ou "sair".')

