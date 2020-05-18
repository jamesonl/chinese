import os
import random
import genanki
import uuid
from .anki.model import anki_model
from .anki.deckid import deck_id_list, model_ids

# I am working through trying to understand how to properly upload cards
# to a package. There are a few bugs that have emerged from this process:
# - Multiple card types emerge | https://anki.tenderapp.com/discussions/ankidesktop/15575-deleting-card-types
# - I am not sure what the right workflow should be to reissue and upload packages to anki
# - It is unclear how to get Anki to automatically consume the latest package that I have uploaded
# - I need to persist model information somewhere
# - I potentially need to persist card ID information somewhere

def create_anki_package(output, cards, deck_name):

    # Assign cards to an existing deck name, otherwise
    # generate a new id and persist this into the model
    # dictionary
    if deck_name in deck_id_list:
        pass
    else:
        # TODO: add a new dictionary value with a key
        pass

    deck_id = deck_id_list[deck_name]

    my_deck = genanki.Deck(
      deck_id,
      deck_name)

    model_id = model_ids[deck_name]
    model = anki_model(model_id)

    for word in cards:
        note = genanki.Note(
            sort_field=1,
            model=model,
            fields=[word.word, word.pinyin, word.definition]
        )
        my_deck.add_note(note)

    output_location = os.path.join(output, "testOutput.apkg")
    genanki.Package(my_deck).write_to_file(output_location)
