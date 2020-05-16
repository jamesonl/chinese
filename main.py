import os
from pipeline.classes.chinese_repo import Structure
from pipeline.card_manager import collect_cards, output_cards


zh_struct = Structure()
cards = collect_cards(zh_struct)

unique_lessons = set([x.lesson for x in cards])
output_cards(zh_struct.packages)
