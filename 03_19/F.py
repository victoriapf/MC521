if __name__ == '__main__':
    papel, resto = map(int, input().split())
    ships = 0
    while resto > 0:
        ships = ships + int(papel/resto)
        novo_resto = papel % resto
        papel = resto
        resto = novo_resto
        if papel < resto:
            papel, resto = resto, papel
    print(ships)
