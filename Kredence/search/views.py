from django.shortcuts import render
from django.db.models import Q

from forum.models import Discussion

def search_view(request):
    query = request.GET.get('q')
    matches = Discussion.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))

    context = {
        "title": "Search",
        "results": matches
    }

    return render(request, "search/results.html", context)



