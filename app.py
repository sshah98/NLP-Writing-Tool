import os
from flask import Flask, url_for, render_template, request, redirect, session, Markup, flash

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
app.secret_key = 'random-key'

from google_npl import GoogleNLP
from email_stats import EmailStats


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == "POST":

        try:

            user_text = request.form['writing']
            word_count = EmailStats(user_text).word_count()
            get_text_easiness = EmailStats(user_text).get_text_easiness()
            sentence_count = EmailStats(user_text).sentence_count()
            subjectivity = EmailStats(user_text).subjectivity()
            complex_words = EmailStats(user_text).complex_words()
            sentiment = GoogleNLP(user_text).sentiment_text()
            sentiment_score, sentiment_mag = sentiment.split(' ')
            
            print(word_count, get_text_easiness, sentence_count, subjectivity, complex_words, sentiment_score, sentiment_mag)

            return render_template('index.html', results=[('Word Count', word_count), ('Sentence Count', sentence_count), ('Readability', get_text_easiness), ('Subjectivity', subjectivity), ('Complex Words', complex_words), ('Sentiment Score', sentiment_score), ('Sentiment Strength', sentiment_mag)])

        except Exception as e:
            flash('Error', e)
            return render_template('index.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
