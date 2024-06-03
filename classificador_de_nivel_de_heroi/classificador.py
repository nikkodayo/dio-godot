while True:
    nome = input("Informe o nome do heroi ou q para sair: ")
    if nome == "q":
        break
    xp = float(input("Informe o xp: "))


    if xp < 1.001:
        nivel = "Ferro"
    elif xp > 1.000 and xp < 2.001:
        nivel = "Bronze"
    elif xp > 2.000 and xp < 5.001:
        nivel = "Prata"
    elif xp > 5.000 and xp < 7.001:
        nivel = "Ouro"
    elif xp > 7.000 and xp < 8.001:
        nivel = "Platina"
    elif xp > 8.000 and xp < 9.001:
        nivel = "Ascendente"
    elif xp > 9.000 and xp < 10.001:
        nivel = "Imortal"
    elif xp >= 10.001:
        nivel = "Radiante"
    print("O Herói de nome " + nome + " está no nível de " + nivel)
