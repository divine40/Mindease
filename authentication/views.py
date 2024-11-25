import json
from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from authentication.models import CustomUser as User
from django.contrib import messages
from django.contrib import auth


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone_number = request.POST["phone_number"]

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(email=email):
            if (len(password) < 5):
                messages.error(request, "Password too short")
                return render(request, 'authentication/register.html', context)

            user = User.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number
            )
            user.set_password(password)
            user.is_active = True
            user.save()

            messages.success(request, "Account Created Successfully")
            return redirect('login')
            # return render(request, 'authentication/register.html')

        return render(request, 'authentication/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]

        if email and password:
            user = auth.authenticate(email=email, password=password)
            print('YES')

            if user:
                print('YES')
                if user.is_active:
                    print('YES')
                    auth.login(request, user)
                    return redirect("/")

                messages.error(
                    request, 'Account is not active, please check your email')
                return render(request, 'authentication/login.html')

            messages.error(request, 'Invalid credentials, try again')
            return render(request, 'authentication/login.html')

        messages.error(request, 'Please fill all fields')
        return render(request, 'authentication/login.html')


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        messages.success(request, "You have been logged out")
        return redirect("login")

    def post(self, request):
        auth.logout(request)
        messages.success(request, "You have been logged out")
        return redirect("login")
