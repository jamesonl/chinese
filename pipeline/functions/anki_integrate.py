import os
import random
import genanki
import uuid

# I am working through trying to understand how to properly upload cards
# to a package. There are a few bugs that have emerged from this process:
# - Multiple card types emerge | https://anki.tenderapp.com/discussions/ankidesktop/15575-deleting-card-types
# - I am not sure what the right workflow should be to reissue and upload packages to anki
# - It is unclear how to get Anki to automatically consume the latest package that I have uploaded
# - I need to persist model information somewhere
# - I potentially need to persist card ID information somewhere

def create_anki_package(output, cards, deck_name, ):
    # using UUID.UUID1 to generate random card #s

    id_list = []
    for i in range(len(cards)):
        id_val = int(str(uuid.uuid1().int)[0:10])
        id_list.append(id_val)

    model = genanki.Model(
      id_list[-1],
      'Simple Model',
      fields=[
        {'name': 'Meaning'},
        {'name': 'Pinyin'},
        {'name': 'Definition'},
        {'name': 'Tags'}
      ],
      templates=[
          {
            'name': 'Only Card', \
              'qfmt': '<center>Define the Following:<div style="font-family: Arial; font-size: \
                      40px; padding: 20px;">{{Meaning}}</div></center>', \
              'afmt': '<center>{{FrontSide}}<hr id=answer><div style="font-family: Arial; \
                      font-size: 20px; padding: 20px;">{{Pinyin}}</div><div \
                      style="font-family: Arial; font-size: 20px; padding: 20px;"> \
                      <em>{{Definition}}</em></div></center>', \
          },
      ])

    # I have no idea what this does
    del id_list[-1]

    #
    my_deck = genanki.Deck(
      id_list[-1],
      'mandarin')

    i = 0

    for word in cards:
        note = genanki.Note(
            # sort_field=id_list[i],
            model=model,
            fields=[word.word, word.pinyin, word.definition]
        )
        my_deck.add_note(note)
        i += 1

    output_location = os.path.join(output, "testOutput.apkg")
    genanki.Package(my_deck).write_to_file(output_location)
