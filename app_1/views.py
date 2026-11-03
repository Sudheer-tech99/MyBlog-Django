from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Post, Category

# Create your views here.
def Home(req):
    posts = Post.objects.all().order_by('-created_at')

    recent_posts = Post.objects.all().order_by('-created_at')[:3]

    categories = Category.objects.annotate(
        post_count=Count('post')
    )

    context = {
        'posts': posts,
        'categories': categories,
        'recent_posts': recent_posts
    }

    return render(req, "Home.html", context)

def Base(req):
    return render(req,'Base.html')

def Allnewpost(req):
    posts = Post.objects.all().order_by('-created_at')

    context = {
        'posts': posts
    }

    return render(req, 'Allposts.html', context)

def Allcategories(req):
    categories = Category.objects.annotate(
        post_count=Count('post')
    )

    context = {
        'categories': categories
    }

    return render(req, 'Allcategories.html', context)

def Addpost(req):
    categories = Category.objects.all()

    if req.method == 'POST':
        title = req.POST.get('title')
        slug = req.POST.get('slug')
        category_id = req.POST.get('category')
        author = req.POST.get('author')
        content = req.POST.get('content')
        status = req.POST.get('status')

        # Check whether slug already exists
        if Post.objects.filter(slug=slug).exists():
            messages.error(req, 'This slug already exists. Please enter a different slug.')

            context = {
                'categories': categories,
                'title': title,
                'slug': slug,
                'category_id': category_id,
                'author': author,
                'content': content,
                'status': status
            }

            return render(req, 'Addpost.html', context)

        category = Category.objects.get(id=category_id)

        Post.objects.create(
            title=title,
            slug=slug,
            category=category,
            author=author,
            content=content,
            status=status
        )

        messages.success(req, 'Your blog post was created successfully!')

        return redirect('Allnewpost')

    context = {
        'categories': categories
    }

    return render(req, 'Addpost.html', context)

def Blogdetails(req, post_id):
    post = Post.objects.get(id=post_id)

    categories = Category.objects.annotate(
        post_count=Count('post')
    )

    context = {
        'post': post,
        'categories': categories
    }

    return render(req, 'Blogdetails.html', context)

def Deletepost(req, post_id):
    post = Post.objects.get(id=post_id)

    if req.method == 'POST':
        post.delete()
        messages.success(req, 'Post deleted successfully!')
        return redirect('Allnewpost')

    return render(req, 'Deletepost.html', {'post': post})

def Cetagory(req, category_id):
    category = Category.objects.get(id=category_id)

    posts = Post.objects.filter(category=category).order_by('-created_at')

    context = {
        'category': category,
        'posts': posts
    }

    return render(req, 'Cetagory.html', context)

def Login(req):
    return render(req,'Login.html')

def Register(req):
    return render(req,'Register.html')