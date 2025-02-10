from django.shortcuts import redirect, render
from django.contrib import messages

from course.views import show
# Create your views here.
from .form import StudentForm

def register(req):
    if req.method == "POST":
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Student Resgister Successfully")
            return redirect(show)
        else:
          
            messages.warning(req, form.errors)
        
            return redirect(register)
    else:
        form = StudentForm()
        
        return render(req, 'student/register.html', {'form': form})
    
    