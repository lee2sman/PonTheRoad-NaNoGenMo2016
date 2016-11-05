#!/usr/bin/env python
# Pon The Road Markov generator
# Lee2sman 2016 cc0
# requires markovify. pip install markovify

import markovify
import random

# Get raw text as string.
with open("source.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

for i in range(250):
    # Print five randomly-generated sentences
    for i in range(random.randint(3,10)):
        print(text_model.make_sentence())
    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(random.randint(5,10)):
        print(text_model.make_short_sentence(140))
    print("")
