
class ChineseCard(object):
    """docstring for ChineseCard."""

    def __init__(self, attr_dict, content):
        super(ChineseCard, self).__init__()
        self.self = self
        self.title = attr_dict['title']
        self.lesson = attr_dict['lesson']
        self.date = attr_dict['date']
        self.content = content.split(" - ")
        self.word = self.content[0]
        self.pinyin = self.content[1]
        self.definition = self.content[2]
