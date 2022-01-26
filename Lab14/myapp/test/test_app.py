#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import numpy as np

# from app import hello, extract_sentiment, text_contains_word, bubble_sort
from app import bubble_sort

# def test_hello():
#     assert hello("Aleksandra") == "Hello Aleksandra"


# test_data_1 = ["I think today will be a great day", "I do not think this will turn out well"]
#
#
# @pytest.mark.parametrize("sample", test_data_1)
# def test_extract_sentiment(sample):
#     assert extract_sentiment(sample) > 0


# test_data_2 = [("There is a duck in this text", "duck", True), ("There is nothing here", "duck", False)]
#
#
# @pytest.mark.parametrize("sample, word, expected_output", test_data_2)
# def test_text_contains_word(sample, word, expected_output):
#     assert text_contains_word(word, sample) == expected_output

float_array = list(np.random.uniform(size=(1, 20)))
sort_arrays = [([3, 0, 6, 9, 8, 7, 4], [0, 3, 4, 6, 7, 8, 9]), ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
               ([i for i in range(20)], [i for i in range(20)]),
               ([i for i in range(30 - 1, -1, -1)], [i for i in range(30)]),
               (float_array, sorted(float_array))]


@pytest.mark.parametrize("input_array, output_array", sort_arrays)
def test_bubble_sort(input_array, output_array):
    assert bubble_sort(input_array) == output_array
