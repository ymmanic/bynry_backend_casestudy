from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Customer, ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.customer = request.user.customer  
            form.save()
            return redirect('success')
    else:
        form = ServiceRequestForm()
    return render(request, 'consumer_services/submit_request_form.html', {'form': form})

def success(request):
    return render(request, 'consumer_services/success.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('submit_request')  # Redirect to request submission page
        else:
            # Handle invalid login credentials
            return render(request, 'consumer_services/login.html', {'error': 'Invalid username or password'})
    return render(request, 'consumer_services/login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def view_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user.customer)  
    return render(request, 'consumer_services/view_requests.html', {'requests': requests})

