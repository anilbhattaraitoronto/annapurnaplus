from django.shortcuts import render
from posts.models import Blog, Event
import datetime


def home_view(request):

    featured_blog = Blog.objects.filter(is_featured=True).last()
    upcoming_events = Event.objects.filter(
        event_date__gte=datetime.date.today())
    context = {
        'featured_blog': featured_blog,
        'upcoming_events': upcoming_events
    }
    return render(request, 'home/index.html', context)


def about_view(request):
    return render(request, 'home/about.html')


def contact_view(request):
    return render(request, 'home/contact.html')
