from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from blogengine.models import Post, Category


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


def getCategory(request, categorySlug, selected_page=1):
    # Get specified category
    posts = Post.get.objects.all().order_by('-pub_date')
    category_posts = []
    for post in posts:
        if post.categories.filter(slug=categorySlug):
            category_posts.append(post)

    pages = Paginator(category_posts, 5)

    category = Category.objects.filter(slug=categorySlug)[0]

    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
    return render_to_response('category.html', {'posts': returned_page.object_list, 'page': returned_page, 'category': category})
