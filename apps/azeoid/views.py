from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegistrationForm, AzeoProfileForm, ProfileUpdateForm
from .models import AzeoProfile

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = AzeoProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            # Profile is created automatically via signal
            profile = user.azeoprofile
            profile.college = profile_form.cleaned_data['college']
            profile.department = profile_form.cleaned_data['department']
            profile.year_of_study = profile_form.cleaned_data['year_of_study']
            profile.phone = profile_form.cleaned_data['phone']
            profile.save()
            
            messages.success(request, f'Your AzeoID has been created: {profile.azeo_id}')
            login(request, user)
            return redirect('azeoid:profile')
    else:
        user_form = UserRegistrationForm()
        profile_form = AzeoProfileForm()
    
    return render(request, 'azeoid/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'title': 'Register'
    })

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.azeoprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('azeoid:profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.azeoprofile)

    return render(request, 'azeoid/profile.html', {
        'profile_form': profile_form,
        'title': 'Profile'
    })

@login_required
def dashboard(request):
    user_profile = request.user.azeoprofile
    context = {
        'user_profile': user_profile,
        'title': 'Dashboard'
    }
    return render(request, 'azeoid/dashboard.html', context)

def verify_azeoid(request):
    if request.method == 'POST':
        azeo_id = request.POST.get('azeo_id')
        try:
            profile = AzeoProfile.objects.get(azeo_id=azeo_id)
            return render(request, 'azeoid/verify_result.html', {
                'profile': profile,
                'valid': True
            })
        except AzeoProfile.DoesNotExist:
            return render(request, 'azeoid/verify_result.html', {
                'valid': False
            })
    return render(request, 'azeoid/verify.html')