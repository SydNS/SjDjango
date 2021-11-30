from django.shortcuts import render


# Create your views here.
def home(request):

    return render(request, 'profileapp/index.html')


def loginuser(request):
    info = {
        "apple": "green",
        "banana": "yellow",
        "cherry": "red"
    }
    return render(request, 'governanceandcontrol/login.html', info)
