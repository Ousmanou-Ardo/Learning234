from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'head.html')

def index(request):
    return render(request, 'bas1.html')

#about us
def mission(request):
    return render(request, 'about-us.html')

def dirigeants(request):
    return render(request, 'features.html')

def conference(request):
    return render(request, 'pricing.html')



#our work
def peace(request):
    return render(request, 'peace.html')

def simulation(request):
    return render(request, 'hire-me.html')

def humanity(request):
    return render(request, 'cv.html')

def sustainable(request):
    return render(request, 'index2.html')


#get involved
def involved(request):
    return render(request, 'contact-us.html')

#corrona
def corona(request):
    return render(request, 'projects-grid-cards.html')