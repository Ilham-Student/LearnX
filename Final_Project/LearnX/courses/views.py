from django.shortcuts import render, get_object_or_404
from .models import Course, Video

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    videos = course.videos.all()
    return render(request, 'course_detail.html', {'course': course, 'videos': videos})

def video_detail(request, course_id, video_id):
    course = get_object_or_404(Course, id=course_id)
    video = get_object_or_404(Video, id=video_id, course=course)
    return render(request, 'video_detail.html', {
        'course': course,
        'video': video
    })
