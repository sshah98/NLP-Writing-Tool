from textblob import TextBlob
# from google_npl import GoogleNLP
from textstat.textstat import textstat

import language_check

# export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_KEY_FILE

class EmailStats(object):

    def __init__(self, string):

        self.string = string
        # self.text_analyzer = GoogleNLP(self.string)
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
        return self.blob.sentiment.subjectivity

    def total_emotion(self):

        tot_score, tot_magnitude = self.text_analyzer.sentiment_text()

        # returns words with scores
        # score is positivity
        # magnitude is strength of sentence
        return '{}${}'.format(str(tot_score), str(tot_magnitude))
    
    def important_entities(self):

        # returns a list with salient words
        return self.text_analyzer.entities_text(self.string)

    def complex_words(self):
        
        # returns list of words with multiple syllables
        return textstat.difficult_words(self.string)
    
string = 'I am happy today'
myobj = EmailStats(string)
print(myobj.get_text_easiness())



