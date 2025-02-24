from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index_view(request):
    return render(request, 'index.html')


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
    return render(request, 'index.html')


@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = request.POST
        fullname = request.POST['fullname']
        password = request.POST['password']
        email = request.POST['email']
        username = request.POST['username']

        print(username, password, email, fullname)
    return render(request, 'index.html')