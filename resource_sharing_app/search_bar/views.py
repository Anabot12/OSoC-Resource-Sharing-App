# views.py
from django.shortcuts import render
from django.db.models import Q

from .models import Resource

def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Perform a case-insensitive search on both the title and tags of resources
        results = Resource.objects.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()

    return render(request, 'search_bar/search_results.html', {'query': query, 'results': results})
