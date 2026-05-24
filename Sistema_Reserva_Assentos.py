assentos = [[False for cl in range(4)] for fl in range(6)]

while True:
    print("Fileira | Coluna")
    print("            A     B     C     D")
    for fl in range(6):
        print(fl + 1, end="       | ")

        for cl in range(4):
            if assentos[fl][cl]:
                simbolo = "X"
            else:
                simbolo = " "

            print("[",simbolo,"]", end=" ")
        print()

    print("\nEscolha seu assento")
    print("Para sair digite 0")
    reserva = str(input("Insira seu assento. Exemplo (2B): ")).upper()

    if reserva == "0":
        print("Encerrando...")
        break

    if len(reserva) != 2:
        print("Escolha um assento correto")
        print("Exemplo: 2B")
        print("##################################")
        input("Pressione ENTER para continuar")
        continue

    if not reserva[0].isdigit() or not reserva[1].isalpha():
        print("Formato incorreto")
        print("Exemplo: 2B")
        print("#################################")
        input("Pressione ENTER para continuar")
        continue

    fl = int(reserva[0]) - 1
    cl = ord(reserva[1]) - ord('A')

    if fl < 0 or fl > 5:
        print("Escolha uma fileira correta")
        print("Exitem 6 fileiras")
        input("Pressione ENTER para continuar")
        continue
    if cl < 0 or cl > 3:
        print("Escolha uma coluna correta")
        print("Exitem 4 colunas")
        input("Pressione ENTER para continuar")
        continue

    if not assentos[fl][cl]:
        print("\nAssento reservado com sucesso!")
        print("Fileira: ", reserva[0], "| Coluna: ", reserva[1])
        assentos[fl][cl] = True
        input("Pressione ENTER para continuar")
        continue
    else:
        print("\nAssento ocupado, escolha outro assento")
        print("Fileira: ", fl + 1)
        print("Coluna: ", cl)
        print("######################################")
        input("Pressione ENTER para continuar")
        continue

