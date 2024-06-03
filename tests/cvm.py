import string

import pytest

from src.cvm import cvm, read_text_to_words, coin_toss, round_zero, round_n


def test_it_should_return_an_int_between_3900_4100():
    result = cvm()
    assert 3900 < result < 4100


@pytest.mark.parametrize(
    "filename,expected",
    [('../numbers-1-100.txt', 100),
     ('../mixedbag.txt', 5)]
)
def test_read_text_to_words(filename: string, expected: int):
    words = read_text_to_words(filename)
    assert len(words) == expected


def test_coin_toss_should_be_random():
    tosses = {True: 0, False: 0}
    for _ in range(1,101):
        tosses[coin_toss()] += 1

    assert 40 < tosses[True] < 60
    assert 40 < tosses[False] < 60


def test_round_zero_has_around_fifty_words():
    words = round_zero(read_text_to_words('../numbers-1-100.txt'))
    assert 30 < len(words) < 70


def test_round_one_has_around_fifty_words():
    stream = read_text_to_words('../numbers-1-200.txt')
    words = round_n(stream, round_zero(stream), 1)
    assert 30 < len(words) < 70


def test_round_one_has_around_fifty_words_with_dupes():
    stream = read_text_to_words('../numbers-1-100.txt')
    dupe_stream = stream + read_text_to_words('../numbers-1-100.txt')
    words = round_n(dupe_stream, round_zero(dupe_stream), 1)
    assert 30 < len(words) < 70

