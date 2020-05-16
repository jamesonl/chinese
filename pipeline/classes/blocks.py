class concept(object):
    """docstring for concept."""

    def __init__(self, word, pinyin, definition, example, zhpy, en_translation):
        super(concept, self).__init__()
        self.self = self
        self.word = word
        self.pinyin = pinyin
        self.definition = definition
        self.example = example
        self.zhpy = zhpy
        self.en_translation = en_translation
