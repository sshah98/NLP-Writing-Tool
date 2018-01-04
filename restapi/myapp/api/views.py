from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json


from . import google_npl
# from . import email_stats
# from email_stats import EmailStats
# from . import email_stats

import logging

logger = logging.getLogger(__name__)

def test(request):
    logger.debug('Inside test url', exc_info=1)
    
    return HttpResponse(json.dumps({'status': 'up'}), content_type='application/json')
    
def google(request):
    
    my_string = request.GET['string']
    myObj = google_npl.GoogleNLP(my_string)
    sentiment_score = myObj.sentiment_text()
    
    ret_response = {}
    ret_response['Sentiment_Score'] = sentiment_score
    
    return HttpResponse(json.dumps(ret_response), content_type='application/json')