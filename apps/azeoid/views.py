from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm

def register_student(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            
            # Send registration confirmation email
            subject = 'Registration Confirmation'
            message = f"""
            Dear {student.name},
            
            Thank you for registering! Your unique AzeoID is: {student.azeoid}
            
            Registration Details:
            Name: {student.name}
            College: {student.college_name}
            Year of Study: {student.year_of_study}
            Phone: {student.phone_number}
            Email: {student.email}
            
            Regards,
            Registration Team
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [student.email]
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            return redirect('registration_success')  # Create this URL
    else:
        form = RegistrationForm()
    
    return render(request, 'azeoid/register.html', {'form': form})

def registration_success(request):
    return render(request, 'success.html')