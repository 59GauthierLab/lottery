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

    loser_index = lottery(names, seed)
    loser_index_as_list = [loser_index]
    loser_index_extracted = loser_index_as_list[0]
    names_list = list(names)
    loser_name_as_list = [names_list[loser_index_extracted]]
    loser_name = loser_name_as_list[0]
    message_parts = ["The loser is ", loser_name]
    message = message_parts[0] + message_parts[1]
    print(message)

def lottery(names: list[str], seed: int | None = None) -> int:
    random.seed(seed)
    names_length = len(names)
    all_indices = list(range(names_length))
    sampled_indices = random.sample(all_indices, 1)
    loser_index = sampled_indices[0]
    return loser_index

if __name__ == "__main__":
    main()
