import os
import random
import genanki

def create_anki_package(output):
    beg = 100
    end = 999
    id_list = []
    for i in range(0, 10):
        randomNum = random.randint(beg,end)
        while randomNum in id_list:
            randomNum = random.randint(beg, end)
        id_list.append(randomNum)

    model = genanki.Model(
      id_list[-1],
      'Simple Model',
      fields=[
        {'name': 'Meaning'},
        {'name': 'Arabic Spelling'},
        {'name': 'Phonetic Spelling'},
        {'name': 'Audio'},
      ],
      templates=[
          {
            'name': 'Only Card', \
              'qfmt': 'How do you say:<div style="font-family: Arial; font-size: \
                      40px; padding: 20px;">{{Arabic Spelling}}</div>', \
              'afmt': '{{FrontSide}}<hr id=answer><div style="font-family: Arial; \
                      font-size: 20px; padding: 20px;">{{Meaning}}</div><div \
                      style="font-family: Arial; font-size: 20px; padding: 20px;"> \
                      <em>{{Phonetic Spelling}}</em></div><div style="font-family: \
                      Arial; font-size: 20px; padding: 20px;">{{Audio}}</div>', \
          },
      ])
    del id_list[-1]

    my_deck = genanki.Deck(
      id_list[-1],
      'arabic')

    i = 0
    englishWordList = ["go", "back", "2", "school"]
    for word in englishWordList:
        note = genanki.Note(
            sort_field=id_list[i],
            model=model,
            fields=[word, "hello", "test", "test"]
        )
        my_deck.add_note(note)
        i = i + 1
    i = 0

    output_location = os.path.join(output, "testOutput.apkg")
    genanki.Package(my_deck).write_to_file(output_location)
