from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import FarmVisitForm
from .models import FarmVisit, FarmPhoto
from django.http import JsonResponse

def farm_visit_form(request):
    if request.method == 'POST':
        form = FarmVisitForm(request.POST, request.FILES)
        if form.is_valid():
            visit = form.save()
            
            # Handle multiple photo uploads
            files = request.FILES.getlist('photos')
            for f in files:
                photo = FarmPhoto.objects.create(image=f)
                visit.additional_photos.add(photo)
            
            messages.success(request, 'Farm visit recorded successfully!')
            
            # Return JSON response for AJAX requests
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Farm visit recorded successfully!'})
            
            # Regular form submission redirect
            if request.user.is_authenticated:
                return redirect('farm_visit_list')
            else:
                return redirect('farm_visit_form')
    else:
        form = FarmVisitForm()
    
    return render(request, 'farmvisit/farm_visit_form.html', {'form': form})

def farm_visit_list(request):
    visits = FarmVisit.objects.all().order_by('-visit_date')
    return render(request, 'farmvisit/farm_visit_list.html', {'visits': visits})

def farm_visit_detail(request, pk):
    visit = get_object_or_404(FarmVisit, pk=pk)
    return render(request, 'farmvisit/farm_visit_detail.html', {'visit': visit})

def farm_visit_edit(request, pk):
    visit = get_object_or_404(FarmVisit, pk=pk)
    if request.method == 'POST':
        form = FarmVisitForm(request.POST, request.FILES, instance=visit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Farm visit updated successfully!')
            return redirect('farm_visit_detail', pk=visit.pk)
    else:
        form = FarmVisitForm(instance=visit)
    
    return render(request, 'farmvisit/farm_visit_form.html', {'form': form, 'edit_mode': True})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('farm_visit_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'farmvisit/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('farm_visit_form')
