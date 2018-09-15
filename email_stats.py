from textblob import TextBlob
from textstat.textstat import textstat

class EmailStats(object):

    def __init__(self, string):

        self.string = string
        self.blob = TextBlob(self.string)

    def get_text_easiness(self):

        # returns integer
        return textstat.flesch_reading_ease(self.string)

    def sentence_count(self):

        # returns integer
        return len(self.blob.sentences)

    def word_count(self):

        # returns integer
        return len(self.blob.words)

    def subjectivity(self):

        # returns integer
        # return "{:.1f}".format(self.blob.sentiment.subjectivity)
        return float(round(self.blob.sentiment.subjectivity, 2)) * 100.0

    def complex_words(self):

        # returns list of words with multiple syllables
        return textstat.difficult_words(self.string)
