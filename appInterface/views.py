from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from . models import polls


def polls_list(request):
    MAX_OBJECTS = 20
    poll = polls.objects.all()[:MAX_OBJECTS]
    data = {"results": list(poll.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)


def polls_details(request, pk):
    poll = get_object_or_404(polls, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}

    return JsonResponse(data)





