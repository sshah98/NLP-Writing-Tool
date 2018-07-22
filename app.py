import os
from flask import Flask, url_for, render_template, request, redirect, session, Markup
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'nlp-analysis-key.json'

from google_npl import GoogleNLP
from email_stats import EmailStats


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == "POST":

        user_text = request.form['writing']
        word_count = EmailStats(user_text).word_count()
        get_text_easiness = EmailStats(user_text).get_text_easiness()
        sentence_count = EmailStats(user_text).sentence_count()
        subjectivity = EmailStats(user_text).subjectivity()
        complex_words = EmailStats(user_text).complex_words()
        # print(sentiment)
        sentiment = GoogleNLP(user_text).sentiment_text()
        print(sentiment)
        
        

        return render_template('index.html', results=0)


if __name__ == '__main__':
    app.run(debug=True)
