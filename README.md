# Sentiment analysis for emails. Used by a chrome extension

## Will continuously update

###Left off at making a django rest api for the email-stats
###Will then follow up with connecting it to a chrome extension


### To use, download/clone files
Install using pip install -r requirements.txt
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account.json
  
Install nltk - punkt because of textblob
# 1st way to do it: 
##python -m textblob.download_corpora

## if that does not work:
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()



### once inside the gui, download "punkt" model in "models"
