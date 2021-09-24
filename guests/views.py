from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Party


def index(request):
    parties = Party.objects.order_by("name")
    return render(request, "guests/index.html", {"parties": parties})

def detail(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    return render(request, "guests/detail.html", {"party": party})

def modify(request, party_id):
    return HttpResponse(f"Modifying party {party_id}")
