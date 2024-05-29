while True:
    print('-'*30)

    opcoes = input("Selecione uma das opções: \n[1]somar, [2]subtrair, [3]multiplicar, [4]dividir, [5]sair: ")
    opcoes_int = int(opcoes)

    if opcoes_int == 5:
        print("Finalizando calculadora.")
        break
    elif opcoes_int <= 4:
        num_1 = input("Primeiro número: ")
        num_2 = input("Segundo número: ")
    else:
        print("Opção inválida! Tente novamente")
        continue

    try:

        if opcoes_int == 1:
            soma = float(num_1) + float(num_2)
            print(soma)
        elif opcoes_int == 2:
            subtracao = float(num_1) - float(num_2)
            print(subtracao)
        elif opcoes_int == 3:
            multiplicacao = float(num_1) * float(num_2)
            print(multiplicacao)
        elif opcoes_int == 4:
            divisao = float(num_1) / float(num_2)
            print(divisao)

        sair = input("\nDeseja sair sair? [s]im ou [n]ão ").lower().startswith("s")

        if sair:
            break
        else:
            continue

    except ValueError:
        print("\nPrimeiro ou segundo número inválido! Tente novamente.")

