from django.shortcuts import render


def post_list(request):
    return render(request, 'polls/post_list.html', {})



