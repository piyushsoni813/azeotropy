from django.shortcuts import render

def header(request):
    return render(request, 'main/header.html')  # Use relative path

def home(request):
    return render(request, 'main/home.html')  # Use relative path

def footer(request):
    return render(request, 'main/footer.html')  # Use relative path
