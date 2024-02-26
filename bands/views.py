# RiffMates/bands/views.py
from django.shortcuts import render, get_object_or_404

from bands.models import Musician

def musician(request):
    data = {
        "musicians": Musician.objects.all().order_by('last_name'),
    }

    return render(request, "musician.html", data)


def musicians(request):
    data = {
        'musicians':Musician.objects.all().order_by('last_name'),
    }

    return render(request, "musicians.html", data)