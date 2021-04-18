from django.shortcuts import render, get_object_or_404
from .forms import AddBlogForm

from .models import Category, Blog

from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def blog_list(request):
    return render(request, 'posts/blog_list.html')


def category_blogs(request, slug, category_id=None):
    category = get_object_or_404(Category, id=category_id)
    category_posts = Blog.objects.filter(category__id=category_id)
    context = {
        'category': category,
        'category_posts': category_posts
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


def blog_detail(request, id):
    return render(request, 'posts/blog_detail.html', {})


def people_list(request):
    return render(request, 'posts/people.html', {})


def program_list(request):
    return render(request, 'posts/programs.html', {})
