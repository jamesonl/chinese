import genanki


def anki_model(id_val):
    model = genanki.Model(
      model_id=id_val,
      name='Chinese Model',
      fields=[
        {'name': 'Meaning'},
        {'name': 'Pinyin'},
        {'name': 'Definition'}
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
          },])
    return model
