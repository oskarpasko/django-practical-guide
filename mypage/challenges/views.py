from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

# Create your views here.

def index(request):
    months = list(challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
