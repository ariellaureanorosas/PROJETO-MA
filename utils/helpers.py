def ler_float(mensagem):
    while True:
        try:
            valor = input(mensagem).replace(",", ".")
            valor = float(valor)
            if valor < 0:
                print("  Valor nao pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("  Entrada invalida. Digite um numero valido.")


def ler_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("  Valor nao pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("  Entrada invalida. Digite um numero inteiro.")


def ler_texto(mensagem, obrigatorio=True):
    while True:
        texto = input(mensagem).strip()
        if obrigatorio and not texto:
            print("  Campo obrigatorio.")
            continue
        return texto


def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
