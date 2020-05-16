# Standard Libraries
import os

# Debugging
# from functions.open_files import select_notes
# from classes.chinese_repo import Structure
# from classes.zhcard import ChineseCard

# Production
from .functions.open_files import select_notes
from .classes.chinese_repo import Structure
from .classes.zhcard import ChineseCard
from .functions.anki_integrate import create_anki_package

# This is where I embed the structure of each file
def parse_notes(text, attr_sect, vocab_sect, note_type = 'zh'):
    attributes = []
    content = []
    if note_type == 'zh':
        af = 0
        vf = 0

        for line in text:
            lls = line
            af = af + 1 if (lls == attr_sect) | (af > 0) else af
            vf = vf + 1 if (lls == vocab_sect) | (vf > 0) else vf

            if (af > 1) & (vf == 0) & (len(lls) > 0):
                attributes.append(line)

            if (vf > 1) & (len(line)) > 0:
                content.append(lls)

    # Clean up the content so that it is returned nicely
    # eliminates any duplicates
    clean_content = list(set(content))

    # splits attributes into key, value pairings
    attr_kv = [(key.split(":")[0], key.split(":")[1]) for key in attributes]
    clean_attr = dict(zip([x[0] for x in attr_kv], [x[1] for x in attr_kv]))

    return clean_attr, clean_content

# captures the card class, and assembles information into an anki format
def create_cards(struct, notes, lang_type = 'zh'):
    all_cards = []
    for n in notes:
        note_path = os.path.join(struct.lessons, n)
        with open(note_path, 'r') as note_info:
            text = note_info.read().split('\n')
        note_info.close()

        # TODO: create standard format for capturing notes, refer to README.md pattern
        assembled_text = parse_notes(text, note_type = 'zh', \
                                     attr_sect = '# Attributes', \
                                     vocab_sect = '# Vocabulary')

        # embed the class structure
        if lang_type == 'zh':
            attr = assembled_text[0]
            words = assembled_text[1]
            cards = [ChineseCard(attr, word) for word in words]
            all_cards.append(cards)

    # flatten the lists since the cards carry all the necessary reference info
    flat_cards = [y for x in all_cards for y in x]
    return flat_cards

def collect_cards(zh_struct):
    # instantiate folder structure object
    zh_notes = os.listdir(zh_struct.lessons)

    # Collect a specific set of files to scrape vocab from
    selected_notes = select_notes(zh_notes, '^[cp]+')

    # assemble cards from selected files
    cards = create_cards(zh_struct, selected_notes)
    return cards
