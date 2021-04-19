from .models import Category, Blog, Event
import datetime


def post_context(request):
    latest_blogs = Blog.objects.filter(is_archived=False)
    categories = Category.objects.all()
    upcoming_events = Event.objects.filter(
        event_date__gte=datetime.date.today())

    return {'categories': categories, 'upcoming_events': upcoming_events, 'latest_blogs': latest_blogs}
