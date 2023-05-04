from huffman import huffman

text = "fffeeeeeddddddcccccccbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

code_frequency = {
    "a": "0",
    "b": "10",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111",
}

text_counter = {"a": 57, "b": 22, "c": 7, "d": 6, "e": 5, "f": 3}


def test_huffman():
    assert code_frequency == huffman.huffman(text, 2)


def test_compute_frequencies():
    assert text_counter == huffman.compute_frequencies(text)


# def test_build_table():
#     assert
