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

    loser = lottery(names, seed)
    print(f"The loser is {loser}")

def lottery(names: list[str], seed: int | None = None) -> str:
    random.seed(seed)
    return random.sample(names, 1)[0]

if __name__ == "__main__":
    main()
