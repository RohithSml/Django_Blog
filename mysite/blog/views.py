from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    context = {}
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context['posts'] = posts
    return render(request, 'blog/post_list.html', context)
