from django.urls import path
from .import views

app_name = 'posts'

urlpatterns = [
    path('bloglist', views.blog_list, name='blog_list'),
    path('people', views.people_list, name='people'),
    path('program', views.program_list, name='programs'),
    path('<id>/<slug>', views.blog_detail, name='blog_detail'),
    path('category/<category_id>/<slug>',
         views.category_blogs, name="category_blogs"),


]
