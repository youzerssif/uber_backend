from django.shortcuts import render

# Create your views here.
def home(request):

    data={
        "Welcome":"Welcome Uber"
    }
    return render(request, 'home.html',data)
