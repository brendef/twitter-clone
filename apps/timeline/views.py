from django.shortcuts import render, redirect
from .models import Post, Vote
from django.contrib.auth.models import User

def upvote(request, post_id=None):
    user = User.objects.get(id=request.user.id)
    post = Post.objects.get(id=post_id)

    try:
        vote = Vote.objects.filter(user=user, post=post).latest('created_at')

        if vote.upvoted == True:
            post.upvotes -= 1
            vote.upvoted = False
        else:
            post.upvotes +=1 
            vote.upvoted = True
        
        if vote.downvoted == True:
            post.downvotes -= 1
            vote.downvoted = False
        
        vote.save()

    except Vote.DoesNotExist:
        Vote.objects.create(user=user, post=post, upvoted=True)
        post.upvotes += 1
     
    post.save()
    return redirect('timeline')

def downvote(request, post_id):
    user = User.objects.get(id=request.user.id)
    post = Post.objects.get(id=post_id)

    try:
        vote = Vote.objects.filter(user=user, post=post).latest('created_at')

        if vote.downvoted == True:
            post.downvotes -= 1
            vote.downvoted = False
        else:
            post.downvotes +=1 
            vote.downvoted = True
        
        if vote.upvoted == True:
            post.upvotes -= 1
            vote.upvoted = False

        vote.save()
    except Vote.DoesNotExist:
        Vote.objects.create(user=user, post=post, downvoted=True)
        post.downvotes += 1
     
    post.save()
    return redirect('timeline')
    
def timeline(request):
    user_upvotes = []
    user_downvotes = []
    posts = Post.objects.all()
    posts_count = posts.count()
    if request.user.id:
        user_upvotes = Vote.objects.filter(user=request.user, upvoted=True).values('post')
        user_downvotes = Vote.objects.filter(user=request.user, downvoted=True).values('post')

    user_upvotes_ids = [ id['post'] for id in list(user_upvotes)]
    user_downvotes_ids = [ id['post'] for id in list(user_downvotes)]
    
    context = {
        'posts': posts,
        'posts_count': posts_count,
        'user_upvotes': user_upvotes_ids,
        'user_downvotes': user_downvotes_ids,
    }

    return render(request, 'timeline/timeline.html', context)