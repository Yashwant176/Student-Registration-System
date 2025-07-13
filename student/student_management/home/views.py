from django.shortcuts import render, redirect

def home_view(request):
    if not request.session.get('user'):
        return redirect('login:login')  # or just '/' if that's your login route
    return render(request, 'home.html')