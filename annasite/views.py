from django.shortcuts import render
from posts.models import Blog, Event
import datetime


def home_view(request):
    latest_blogs = Blog.objects.filter(is_archived=False)
    featured_blog = latest_blogs.filter(is_featured=True).first()
    upcoming_events = Event.objects.filter(
        event_date__gte=datetime.date.today())
    context = {
        'latest_blogs': latest_blogs,
        'featured_blog': featured_blog,
        'upcoming_events': upcoming_events
    }
    return render(request, 'home/index.html', context)


def about_view(request):
    return render(request, 'home/about.html')


def contact_view(request):
    return render(request, 'home/contact.html')
