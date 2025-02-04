from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Course  # Make sure you have imported your model


# Create your views here.

def show(request, **kwargs):
    data = kwargs.get('status')
    courses = Course.objects.all().order_by('desc')
    return render(request, 'course/home.html',context = {'courses': courses, 'status': data})


@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        course = Course.objects.filter(name = data.get('name')).first()
        if course:
            return JsonResponse({'msg': 'Course is already register'})
        
        course = Course.objects.create(
            name=data.get('name'),
            desc=data.get('desc'),
            fee = data.get('fee'),
            duration = data.get('duration')
        )
        
        return JsonResponse({'status': 'success', 'id': course.name})
    
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
        