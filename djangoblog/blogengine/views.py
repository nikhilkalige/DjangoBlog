from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from models import Post


def getPosts(request, selected_page=1):
    # get all blog posts
    posts = Post.objects.all().order_by('-pub_date')

    # add pagination
    pages = Paginator(posts, 5)

    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # display all posts
    return render_to_response('posts.html', {'posts': returned_page.object_list, 'page': returned_page, })


def getPost(request, postSlug):
    # Get specified post
    post = Post.objects.filter(slug=postSlug)

    # Display specified post
    return render_to_response('single.html', {'posts': post})
