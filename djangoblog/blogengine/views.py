from django.shortcuts import render_to_response
from models import Post


def getRecentPosts(request):
    posts = Post.objects.all()

    # sort by chronological order
    sorted_posts = posts.order_by('-pub_date')

    # display all posts
    return render_to_response('posts.html', {'po': sorted_posts})
