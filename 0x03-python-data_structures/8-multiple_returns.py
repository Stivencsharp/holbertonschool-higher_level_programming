#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        first_letter = sentence[0]
    else:
        first_letter = None
    return len(sentence), first_letter
