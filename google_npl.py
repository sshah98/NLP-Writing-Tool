import six

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


class GoogleNLP(object):

    def __init__(self, text):

        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')
        self.text = text

        # Create the Google Language API Client
        self.client = language.LanguageServiceClient()

        # Instantiates a plain text document.
        self.document = types.Document(
            content=self.text, type=enums.Document.Type.PLAIN_TEXT)

    def sentiment_text(self):
        """Detects sentiment in the text."""

        # Detects sentiment in the document. You can also analyze HTML with:
        sentiment = self.client.analyze_sentiment(
            self.document).document_sentiment

        return sentiment.score, sentiment.magnitude

    def entities_text(self):
        """Detects entities in the text."""

        entities = self.client.analyze_entities(self.document).entities

        # Adjust the the names of the entities - these are the only ones that are available
        # Each word is associated with one entity_type

        entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                       'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

        important_words = []
        for entity in entities:

            important_words.append(
                (entity.name, entity_type[entity.type], entity.salience))

            # print('=' * 20)
            # print(u'{:<16}: {}'.format('name', entity.name))
            # print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
            # print(u'{:<16}: {}'.format('metadata', entity.metadata))
            # print(u'{:<16}: {}'.format('salience', entity.salience))
            # print(u'{:<16}: {}'.format('wikipedia_url',
            #       entity.metadata.get('wikipedia_url', '-')))

        return important_words

    def syntax_text(self):
        """Detects syntax in the text."""

        tokens = self.client.analyze_syntax(self.document).tokens

        pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
                   'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
        words = []

        for token in tokens:
            words.append((pos_tag[token.part_of_speech.tag],
                          token.text.content))

        return words

