from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Walk for at least 20 minutes every day!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Walk for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Eat no meat for the entire month!",
    "september": "Walk for at least 20 minutes every day!",
    "october": "Holidays!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Holidays!"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenges(request, month):
    try:
        challenge_text = challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
