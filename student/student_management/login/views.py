from django.shortcuts import render, redirect
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "Yash" and password == "12345":
            request.session['user'] = username  # store login info
            return redirect('home:home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    # Already logged in? Send to home
    if request.session.get('user'):
        return redirect('home:home')

    return render(request, 'login.html')
