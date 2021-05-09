import math


def felszin(sugar: float, m: float) -> float:
    return 2 * sugar * math.pi * (sugar + m)


def terfogat(sugar: float, m: float) -> float:
    return sugar ** 2 * math.pi * m


def Main() -> None:
    print('Henger A és V:')
    sugar: float = float(input("Sugár:"))
    m: float = float(input("Magasság:"))
    if sugar <= 0 or m <= 0:
        print('Nincs ilyen henger!')
    else:
        print(f'A henger felszíne: {felszin(sugar, m)}')
        print(f'A henger térfogata: {terfogat(sugar, m)}')


if __name__ == "__main__":
    Main()
