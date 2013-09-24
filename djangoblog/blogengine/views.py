from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from models import Post


def getPosts(request, selected_page=1):
    # get all blog posts
    posts = Post.objects.all().order_by('-pub_date')

    # add pagination
    pages = Paginator(posts, 5)
    returned_page = pages.page(selected_page)

    # display all posts
    return render_to_response('posts.html', {'posts': returned_page.object_list})
