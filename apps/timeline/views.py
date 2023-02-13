from django.shortcuts import render, redirect
from .models import Post, Votes
from django.contrib.auth.models import User

def upvote(request, post_id=None):
    user = User.objects.get(id=request.user.id)
    post = Post.objects.get(id=post_id)

    try:
        vote = Votes.objects.filter(user=user, post=post).latest('created_at')
        if vote.action == True:
            post.upvotes += 1
        else: 
            post.upvotes -= 1
            downvotes -= 1

        Votes.objects.create(user=user, post=post, action=not vote.action)

    except Votes.DoesNotExist:
        Votes.objects.create(user=user, post=post, action=True)
        post.upvotes += 1
     
    post.save()
    return redirect('timeline')

def downvote(request, post_id):
    user = User.objects.get(id=request.user.id)
    post = Post.objects.get(id=post_id)

    try:
        vote = Votes.objects.filter(user=user, post=post).latest('created_at')
        if vote.action == False:
            post.downvotes += 1
        else: 
            post.downvotes -= 1

        Votes.objects.create(user=user, post=post, action=not vote.action)

    except Votes.DoesNotExist:
        Votes.objects.create(user=user, post=post, action=True)
        post.upvotes += 1
     
    post.save()
    return redirect('timeline')

def timeline(request):
    posts = Post.objects.all()
    posts_count = posts.count()
    
    print(posts)
    
    context = {
        'posts': posts,
        'posts_count': posts_count,
    }

    return render(request, 'timeline/timeline.html', context)