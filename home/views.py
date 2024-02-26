import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def credits(request):
    content = "Nicky\nYour Name"

    return HttpResponse(content, content_type="text/plain")

def info_page(request):
    return request(render, "home/info_page.html")

def news(request):
    data = {
        'news':[
            "RiffMates now has a news page!",
            "RiffMates has its first web page",
        ],
    }

    # OR return render(request, "../templates/news.html", data)
    return render(request, "news2.html", data)

def news_advanced(request):
    # Get the current date and time
    current_date = datetime.datetime.now()

    # Assuming 'news_data' is a list of tuples containing (date, subject)
    news_data = [
        (current_date, "RiffMates now has a news page!"),
        (current_date, "RiffMates has its first web page"),
        (current_date, "RiffMates now has a news page!"),
        (current_date, "RiffMates has its first web page"),
        (current_date, "RiffMates now has a news page!"),
        (current_date, "RiffMates has its first web page"),
    ]
    
    return render(request, "news_advanced.html", {
        'news_data': news_data
        })