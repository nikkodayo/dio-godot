def calculadora(vitorias, derrotas):
    return vitorias - derrotas

def rank(vitorias):
    if vitorias <= 10:
        return "Ferro"

    elif vitorias >= 11 and vitorias <= 20:
        return "Bronze"

    elif vitorias >= 21 and vitorias <= 50:
        return "Prata"
    
    elif vitorias >= 51 and vitorias <= 80:
        return "Ouro"

    elif vitorias >= 81 and vitorias <= 90:
        return "Diamante"

    elif vitorias >= 91 and vitorias <= 100:
        return "Lendário"

    elif vitorias >= 101:
        return "Imortal"

def calcular_partidas_rankeadas():
    vitorias = int(input("Digite o numero de vitórias: "))
    derrotas = int(input("Digite o numero de derrotas: "))
    saldo_vitorias = str(calculadora(vitorias, derrotas))
    nivel = rank(vitorias)
    print("O Herói tem saldo de " + saldo_vitorias + " está no nível " + nivel)

calcular_partidas_rankeadas()
