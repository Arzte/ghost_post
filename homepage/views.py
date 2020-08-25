from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Post

from homepage.forms import AddPostForm


def homepage_view(request):
    posts = Post.objects.all().order_by('-submission_time')
    return render(request, 'index.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                boast=data.get('boast'),
                content=data.get('content'),
            )
        return HttpResponseRedirect(reverse('home'))

    form = AddPostForm()
    return render(request, 'generic_form.html', {
        'form': form,
        'name': 'post',
    })


def add_upvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.upvotes = post.upvotes + 1
    post.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_downvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.downvotes = post.downvotes + 1
    post.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def boast_view(request):
    posts = Post.objects.filter(boast=True).order_by('-submission_time')
    return render(request, 'index.html', {'posts': posts})


def roast_view(request):
    posts = Post.objects.filter(boast=False).order_by('-submission_time')
    return render(request, 'index.html', {'posts': posts})


def vote_view(request):
    posts = sorted(Post.objects.all(),
                   key=lambda post: post.score(), reverse=True)
    return render(request, 'index.html', {'posts': posts})
