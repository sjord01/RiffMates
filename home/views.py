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

    return render(request, "../templates/news.html", data)