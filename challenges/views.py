from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == "jan":
        challenge_text = "This works!"
    elif month == "feb":
        challenge_text = "Walk 20 min at day"
    elif month == "mar":
        challenge_text = "Whatever"
    elif month == "apr":
        challenge_text = "Have a good month"
    elif month == "may":
        challenge_text = "Love your mother"
    elif month == "june":
        challenge_text = "Be carefull with the heat"
    elif month == "july":
        challenge_text = "Love your father"
    elif month == "aug":
        challenge_text = "September is coming"
    elif month == "sept":
        challenge_text = "Happy birthday"
    elif month == "oct":
        challenge_text = "This is halloween, halloween, halloween"
    elif month == "nov":
        challenge_text = "The winter is coming"
    elif month == "dec":
        challenge_text = "Merry christmas"
    else:
        return HttpResponseNotFound("This month doesn't exist")

    return HttpResponse(challenge_text)