from django.shortcuts import render, redirect
from .models import Post, Comment
from accounts.models import User
from .forms import AddPost
# Create your views here.
def all_posts(req):
    context = {
        'all_post': Post.objects.all(),
        'all_user': User.objects.all()
    }

    return render(req, 'index.html', context)

def add_post(req):
    if req.method == 'POST':
        form = AddPost(req.POST, req.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = req.user
            post.save()
            return redirect('all_post')
        else:
            return render(req, 'add_post.html', {
                'add_form': form
            })
    context = {
        'add_form': AddPost()
    }
    return render(req, 'add_post.html', context)

def delete_post(req, id):
    found_post = Post.objects.get(id=id)
    found_post.delete()
    return redirect('all_post')

def likes(req, id):
    post = Post.objects.get(id=id)
    current_user = req.user
    if post.likes.filter(id=current_user.id).exists():
        post.likes.remove(current_user)
    else:
        post.likes.add(current_user)
    return redirect('all_post')

def comment(req, id):
    post = Post.objects.get(id=id)
    current_user = req.user

    if req.method == 'POST':
        comment_text = req.POST.get('comment')
        new_comment = Comment(comment=comment_text, post=post, user=current_user)
        new_comment.save()

    context = {
        'all_post': Post.objects.all(),
        'comment': Comment.objects.filter(post=post),
        'comment_post': post
    }
    return render(req, 'index.html', context)