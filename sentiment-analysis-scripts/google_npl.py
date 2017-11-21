import six

from google.cloud import language


class GoogleNLP(object):

    def __init__(self, text):

        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')
        self.text = text

        # Create the Google Language API Client
        self.language_client = language.Client()

    def sentiment_text(self):
        """Detects sentiment in the text."""

        # Instantiates a plain text document.
        document = self.language_client.document_from_text(self.text)

        # Detects sentiment in the document. You can also analyze HTML with:
        #   document.doc_type == language.Document.HTML

        sentiment = document.analyze_sentiment().sentiment

        return sentiment.score, sentiment.magnitude

    def entities_text(self):
        """Detects entities in the text."""

        # Instantiates a plain text document.
        document = self.language_client.document_from_text(self.text)

        # Detects entities in the document. You can also analyze HTML with:
        #   document.doc_type == language.Document.HTML
        entities = document.analyze_entities().entities

        important_words = []
        for entity in entities:
            # print('=' * 20)
            important_words.append(
                (entity.name, entity.entity_type, entity.salience))
            # print(u'{:<16}: {}'.format('metadata', entity.metadata))
            # print(u'{:<16}: {}'.format('wikipedia_url', entity.metadata.get('wikipedia_url', '-')))

        return important_words

    def syntax_text(self):
        """Detects syntax in the text."""

        # Instantiates a plain text document.
        document = self.language_client.document_from_text(self.text)

        # Detects syntax in the document. You can also analyze HTML with:
        #   document.doc_type == language.Document.HTML
        tokens = document.analyze_syntax().tokens

        words = []
        for token in tokens:
            words.append((token.part_of_speech.tag, token.text_content))

        return words
