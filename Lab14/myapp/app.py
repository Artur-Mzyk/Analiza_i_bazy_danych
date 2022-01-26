#!/usr/bin/python
# -*- coding: utf-8 -*-

# from textblob import TextBlob
from typing import List


def hello(name: str):
    return f"Hello {name}"


# def extract_sentiment(text: str):
#     return TextBlob(text).sentiment.polarity


# def text_contains_word(word: str, text: str):
#     return word in text


def bubble_sort(array: List[int]) -> List[int]:
    lst = array[:]
    n = len(lst) - 1

    if_changed = True

    while n > 0 and if_changed:
        if_changed = False

        for i in range(n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                if_changed = True

        n -= 1

    return lst
