from django.shortcuts import render
from models import Poll

def list_view(request):
    context = {"polls": Poll.objects.all()}
    return render(request, "list.html", context)

def detail_view(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {"poll", poll}
    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    return render(request, "detail.html", context)