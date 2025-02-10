from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q,F, Count, Avg, Sum
import json
from .models import Course  # Make sure you have imported your model
from .form import CourseForm, FileForm
import pandas as pd
 

# Create your views here.

def show(request, **kwargs):
    data = kwargs.get('status')
    coursedata = Course.objects.aggregate(
        total__Course = Count("id"),
        averge__fees = Avg('fee'),
        sums__fees = Sum('fee')
    )
    print(coursedata)
    # courses = Course.objects.filter(Q(fee__lt=F('duration') * 100) & Q(duration__lt=4) )
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'course/home.html',context = {'courses': courses,
                                                        'cd': coursedata, 'status': data})
@login_required
@csrf_exempt
def create(request):
    if not request.user.is_authenticated or request.user.user_type != 'teacher':
        messages.error(request, "You are not authorized to create a course.")
        return redirect(show)
    if request.method == 'POST':
        # data = json.loads(request.body)
        # course = Course.objects.filter(name = data.get('name')).first()
        # if course:
        #     return JsonResponse({'msg': 'Course is already register'})
        form_type = request.POST.get('form_type')
        if  form_type == 'from':
            form = CourseForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Course is Create successfully")
            # course = Course.objects.create(
            #     name=data.get('name'),
            #     desc=data.get('desc'),
            #     fee = data.get('fee'),
            #     duration = data.get('duration')
            # )
                return redirect(show)
            else:
                messages.warning(request, "Course is already Create")
                return redirect(show)
        else:
            fileForm = FileForm(request.POST, request.FILES)
            if 'file' in request.FILES:
                fileForm = FileForm(request.POST, request.FILES)
                if fileForm.is_valid():
                    upload_file = fileForm.save()
                    file_path = upload_file.file.path
                    df = pd.read_excel(file_path)
                    df.columns = df.columns.str.lower()
                    for _, row in df.iterrows():
                        course, created = Course.objects.get_or_create(
                            name = row['name'],
                            duration = row['duration'],
                            desc = row['desc'],
                            fee = row['fee'],
                            
                            
                        )
                    if created:
                        messages.success(request, f"Multiple Course is Create successfully")
                    else:
                        messages.warning(request, f"{course.name} is already created")
                    return redirect(show)
                else:
                    messages.warning(request, f"Invalid File: {fileForm.errors}")
                    
                    
                    return redirect(create)
            else:
                messages.warning(request, "Please select a file")
                return redirect(create)


    form = CourseForm()
    fileForm = FileForm()
    return render(request, 'course/create.html',{'status': 'success','form': form, 'filesfrom': fileForm})
    
@csrf_exempt
def update(request):
    if request.method== 'PUT':
        data = json.loads(request.body)
        course = Course.objects.filter(name = data.get('name')).first()
        if not course:
            return JsonResponse({'msg': 'Course is not register'})
        
        course.fee = data.get('fee')
        course.desc = data.get('desc')
        course.duration = data.get('duration')
        course.save()
        
        return redirect(show)
    else:
        
        
        return JsonResponse({'status': 'update successfully', 'name': course.name})
        
        

@csrf_exempt
def delete(request):
    if request.method == 'DELETE':
        data = request.GET.dict()
        
        try:
            course = Course.objects.filter(name=data.get('name')).first()
            if not course:
                return JsonResponse({'msg': 'Course not found'}, status=404)
            course.delete()
            return JsonResponse({'status': 'deleted successfully', 'name': course.name})
        except Course.DoesNotExist:
            return JsonResponse({'msg': 'Course not found'}, status=404)
        