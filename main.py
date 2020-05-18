import os
from pipeline.classes.chinese_repo import Structure
from pipeline.card_manager import collect_cards
from pipeline.functions.anki_integrate import create_anki_package

# instantiate the folder structure
zh_struct = Structure()

# parse the files and construct the card objects
cards = collect_cards(zh_struct)
print("TOTAL CARDS: ", len(cards))

# for demo purposes
print(len(cards))

# get some analytics on the state of the cards I have created
unique_lessons = set([x.lesson for x in cards])

# output a package so that I can consume them into anki
create_anki_package(zh_struct.packages, cards, "mandarin")
