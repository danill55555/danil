from django.contrib.auth import authenticate, logout
from .forms import LoginForm, signUpForm,ApplicationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Application, Status

def index(request):
    return render(request, 'index.html', context={})

def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = signUpForm()
    return render(request, 'registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Некорректный логин или пароль")
        else:
            messages.error(request, "Некорректный логин или пароль")
    else:
        form = LoginForm()
    return render(request=request, template_name="login.html", context={'form':form})


def logout_view(request):
    logout(request)
    return redirect('home')


def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.status = '0'  # Новое
            application.save()
            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'create_application.html', {'form': form})

def user_applications(request):
    if request.user.is_authenticated:
        applications = Application.objects.filter(user=request.user)
        return render(request, 'applications.html', {'applications': applications})
    else:
        return render(request, 'applications.html')  # или любой другой шаблон для неавторизованных пользователей

def application_detail(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    return render(request, 'application_detail.html', {'application': application})

# Администратор

@login_required
def admin_dashboard(request):
    applications = Application.objects.all().order_by('-date_of_submission')

    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        new_status = request.POST.get('status')
        if application_id and new_status:
            application = get_object_or_404(Application, pk=application_id)

            # Сохраняем выбранный статус (строка) в поле status
            application.status = new_status
            application.save()

    return render(request, 'admin_dashboard.html', {'applications': applications})
