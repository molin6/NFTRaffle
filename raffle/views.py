from django.shortcuts import render

def cube(request):
	return render(request, 'cube.html', {})

def home(request):
    return render(request, 'home.html')

def join_raffle(request):
    return render(request, 'join_raffle.html')

def create_raffle(request):
    return render(request, 'create_raffle.html')