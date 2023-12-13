from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Products
from .forms import BookingForm
from django.contrib import messages

# Create your views here.
def index(request):
    product = Products.objects.all()
    return render(request, 'index.html', {'products': product})

def about(request):
    return render(request, 'about.html')



@login_required(login_url='login')
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking')
    else:
        form = BookingForm()

    # Display form errors
    if form.errors:
        for field, error in form.errors.items():
            messages.error(request, f"{field}: {error}")

    return render(request, 'booking.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def menu(request):
    product = Products.objects.all()
    return render(request, 'menu.html', {'products': product})

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')