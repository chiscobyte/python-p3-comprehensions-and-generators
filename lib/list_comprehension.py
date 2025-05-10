#!/usr/bin/env python3

def return_evens(sequence):
    return [n for n in sequence if n % 2 == 0]
print(return_evens(range(1-10)))

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))