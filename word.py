import datetime
import uuid

class Word:
    def __init__(self, value, language, repeat=False):
        self.uuid = uuid.uuid4()
        self.value = value.lower()
        self.language = language
        self.date_create = datetime.datetime.now()
        if repeat == False:
            self.repeat_word = False
            self.repeat_after = None
        else:
            self.repeat_word = True
            self.repeat_after = datetime.datetime.now() + datetime.timedelta(days=1)
        self.translations = []

    def add_translation(self, translation, language):
        if (translation, language) not in self.translations:
            self.translations.append((translation, language))

    def get_all_translations(self):
        return '\n'.join([f'{t[1]}: {t[0]}' for t in self.translations])

    def __repr__(self):
        return f'Слово "{self.value.capitalize()}":\n{self.uuid}\nязык {self.language}\nсоздано {self.date_create}\nповторить до {self.repeat_after}\n{self.get_all_translations()}'


if __name__ == '__main__':
    w = Word('нога', 'ru', True)
    w.add_translation('leg', 'en')
    w.add_translation('foot', 'en')
    w.add_translation('нога', 'ua')
    print(w)
