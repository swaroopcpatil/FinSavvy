from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Register
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "About-us.html")

def ai(request):
    return render(request, "ai.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)  # Automatically log in the user after registration
            return redirect('forminfo')  # Redirect to form info after registration
        else:
            print(form.errors)  # Print form errors to debug
            messages.error(request, "There was a problem with the registration.")
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


# View for handling user login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}')
                return redirect('user_details')  # Redirect to the detail page after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            print(form.errors)  # Debug login errors
            messages.error(request, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'Log-in.html', {'form': form})


# View for handling user logout
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
# def detail(request):
#     user_details = Register.objects.filter(email=request.user.email).first()  # Fetch user details based on email
#     return render(request, "detail.html", {"user_details": user_details})

@login_required
def forminfo(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            # Ensure the user is logged in and has an email
            if request.user.is_authenticated:
                register.email = request.user.email  # Link the form data to the logged-in user
            else:
                messages.error(request, "You must be logged in to submit this form.")
                return redirect('login')  # Redirect to login if not authenticated

            register.save()  # Save the instance to the database
            messages.success(request, "Form info submitted successfully!")
            return redirect('ai')  # Redirect to AI page after form submission
        else:
            # Print form errors for debugging
            print(form.errors)  # Check what errors occurred
    else:
        form = RegisterForm()
    
    return render(request, 'forminfo.html', {'form': form})


@login_required
def user_details(request):
    # Get the user's registration details using their email
    try:
        register = Register.objects.get(email=request.user.email)
    except Register.DoesNotExist:
        messages.error(request, "No registration details found. Please fill the form.")
        return redirect('forminfo')  # Redirect to form if no details found

    return render(request, 'detail.html', {'register': register})

# View for updating user details
@login_required
def update_user_details(request):
    # Check if the logged-in user has a registration record
    try:
        register = Register.objects.get(user=request.user)
    except Register.DoesNotExist:
        # Redirect the user to fill the form if no registration details exist
        messages.error(request, "No registration details found. Please fill the form.")
        return redirect('forminfo')  # Redirect to form if no details found

    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=register)
        if form.is_valid():
            form.save()
            messages.success(request, "Your details were updated successfully!")
            return redirect('user_details')  # Redirect to the details page after update
    else:
        form = RegisterForm(instance=register)

    return render(request, 'update.html', {'form': form})



