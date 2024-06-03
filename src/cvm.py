import random
import string

import num2words


def cvm(file: string) -> int:
    return 4000


def read_text_to_words(filename: string) -> list[string]:
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()

    return words


def round_zero(stream: list[string]) -> list:
    words = []

    while len(words) < 100:
        words.append(stream.pop(0))

    for word in words:
        if not coin_toss():
            words.remove(word)

    return words


def round_n(stream: list[string], words: list[string], head_count: int) -> list:

    while len(words) < 100 and len(stream) > 0:
        word = stream.pop(0)
        if word in words:
            for _ in range(head_count):
                if not coin_toss():
                    words.remove(word)
        else:
            words.append(word)

    for word in words:
        if not coin_toss():
            words.remove(word)

    return words


def coin_toss() -> bool:
    return random.choice([True, False])


def numbers():
    for int in range(1, 201):
        print(num2words.num2words(int))


if __name__ == "__main__":
    numbers()
