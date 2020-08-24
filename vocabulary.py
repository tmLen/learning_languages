from word import Word

class Vocabulary:
    def __init__(self):
        self.my_words = {}

    def is_word_known(self, word, language):
        if (word, language) in self.my_words:
            return True
        return False

    def add_new_word(self, word, word_language, translation, translation_language):

        if not self.is_word_known(word, word_language):
            self.my_words[(word.lower(), word_language)] = Word(word.lower(), word_language)

        if not self.is_word_known(translation, translation_language):
            self.my_words[(translation.lower(), translation_language)] = Word(translation.lower(), translation_language, True)

        self.my_words[(word.lower(), word_language)].add_translation(translation.lower(), translation_language)
        self.my_words[(translation.lower(), translation_language)].add_translation(word.lower(), word_language)

    def __repr__(self):
        return '\n\n'.join([self.my_words[word].__repr__() for word in self.my_words])

if __name__ == '__main__':
    my_vocabulary = Vocabulary()
    my_vocabulary.add_new_word('нога', 'ru', 'leg', 'en')
    my_vocabulary.add_new_word('нога', 'ru', 'leg', 'en')
    my_vocabulary.add_new_word('нога', 'ru', 'foot', 'en')
    my_vocabulary.add_new_word('рука', 'ru', 'hand', 'en')

    print(my_vocabulary)