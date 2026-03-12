import random

def main():
    seed = 9223372036854775783
    names: list[str] = [
        "uchida",
        "urasaki",
        "katano",
        "saito",
        "yonemura",
        "muhoro",
    ]

    winner = lottery(names, seed)
    print(f"The winner is {winner}")

def lottery(names: list[str], seed: int | None = None) -> str:
    random.seed(seed)
    return random.sample(names, 1)[0]

if __name__ == "__main__":
    main()
