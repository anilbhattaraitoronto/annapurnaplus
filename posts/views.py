from django.shortcuts import render, get_object_or_404
from .forms import AddBlogForm

from .models import Category, Blog, Person, Program, Presentation

from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def blog_list(request):
    return render(request, 'posts/blog_list.html')


def category_blogs(request, slug, category_id=None):
    category = get_object_or_404(Category, id=category_id)
    category_blogs = category.blog_set.all()
    print('category blogs are', category_blogs)
    context = {
        'category': category,
        'category_blogs': category_blogs
    }
    return render(request, 'posts/category_posts.html', context)


# def add_blog(request):
#     form = AddBlogForm()
#     context = {
#         'add_post_form': form
#     }
#     if request.method == 'POST':
#         category = request.POST.get('category')
#         title = request.POST.get('title')
#         summary = request.POST.get('summary')
#         content = request.POST.get('summary')
#         is_featured = request.POST.get('is_featured', False)

#         newblog = Blog()
#         newblog.category = category
#         newblog.title = title
#         newblog.summary = summary
#         newblog.content = content
#         newblog.is_featured = True if is_featured == 'on' else False

#         newblog.save()
#         return HttpResponseRedirect(reverse('posts:blog_detail', kwargs={'id': newblog.pk}))
#     return render(request, 'posts/add_blog.html', context)


def blog_detail(request, slug,  id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'posts/blog_detail.html', {'blog': blog})


def people_list(request):
    persons = Person.objects.all()
    presentations = Presentation.objects.all()
    return render(request, 'posts/people.html', {'persons': persons, 'presentations': presentations})


def program_list(request):
    programs = Program.objects.all()
    return render(request, 'posts/programs.html', {'programs': programs})
