
from django.conf import settings
from django.contrib import messages    
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserForm
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Optionally assign the user to a group based on their user_type
            if user.user_type == 'teacher':
                teacher_group, created = Group.objects.get_or_create(name='Teachers')
                teacher_group.user_set.add(user)
            else:
                student_group, created = Group.objects.get_or_create(name='Students')
                student_group.user_set.add(user)

            login(request, user)
            messages.success(request, "You have register Successfully")
            return redirect('login')  
    else:
        form = CustomUserForm()
    return render(request, 'account/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)



class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def form_valid(self, form):
        messages.success(self.request, "You have successfully logged in!")
        return super().form_valid(form)
