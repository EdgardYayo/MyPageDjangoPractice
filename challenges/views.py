from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_abrev = {
    "january":"This works!",
    "february":"Walk 20 min at day",
    "march": "Happy birthday to my mom",
    "april": "Have a good month",
    "may": "Love your mother",
    "june": "Be carefull with the heat",
    "july": "Love your father",
    "august": "September is coming",
    "september": "Happy birthday to me",
    "october": "This is halloween, halloween, halloween",
    "november": "The winter is coming",
    "december": "Merry Christmas"
}

# Create your views here.

def index(request):

    list_items = ""
    months = list(monthly_abrev.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    response_data = f"""
        <ul>
            {list_items}
        </ul>
    """
    return HttpResponse(response_data)

def monthly_by_number(request, month_number):
    # challenge_text = None
    # if month_number == 1:
    #     challenge_text = "This works!"
    # elif month_number == 2:
    #     challenge_text = "Walk 20 min at day"
    # elif month_number == 3:
    #     challenge_text = "Whatever"
    # elif month_number == 4:
    #     challenge_text = "Have a good month"
    # elif month_number == 5:
    #     challenge_text = "Love your mother"
    # elif month_number == 6:
    #     challenge_text = "Be carefull with the heat"
    # elif month_number == 7:
    #     challenge_text = "Love your father"
    # elif month_number == 8:
    #     challenge_text = "September is coming"
    # elif month_number == 9:
    #     challenge_text = "Happy birthday"
    # elif month_number == 10:
    #     challenge_text = "This is halloween, halloween, halloween"
    # elif month_number == 11:
    #     challenge_text = "The winter is coming"
    # elif month_number == 12:
    #     challenge_text = "Merry christmas"
    # else:
    months = list(monthly_abrev.keys())
    if month_number > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month_number - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try: 
        challenge_text = monthly_abrev[month]
        # month_capt = month.capitalize()
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("""<div style="display: flex; align-item:center; justify-content:center; border: 1px solid black; border-radius: 10px;  padding: 10px;">
                                            <h1>This month doesn't exist<h1>
                                            <span>💐</span>
                                        </div>
                                    """)
