from django.shortcuts import render, redirect
from .forms import ListForm, UpdateForm, ProfileDetails, UserForm
from django.shortcuts import render
import logging
from mypost.models import Post, Category, DriverUser
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


def all_posts(request):
    user = request.user.id
    form = ListForm(request.POST)
    posts = Post.objects.filter(author=user).order_by('-id')
    category_search = Category.objects.all()

    if request.method == 'POST':
        category_id = request.POST.get('category_id_f')
        posts = Post.objects.filter(category=category_id, author=user).order_by('-id')

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')

    ##posts = paginator.get_page(page)

    context_posts = {
        'posts': posts,
        'category_search': category_search,
    }

    return render(request, 'user_profile/all_profiles.html', context_posts)


def profile(request):
    user = DriverUser.objects.filter(id=request.user.id).order_by('-id')
    posts = Post.objects.filter(author=user).order_by('-id')
    dict = {}
    for users in user:
        dict['username'] = users.username
        dict['email'] = users.email
        dict['password'] = users.password
        dict['n_user'] = users.pk
        dict['first_name'] = users.first_name

    dict['posts'] = posts
    context_posts = dict
    return render(request, 'user_profile/profile_detail.html', context_posts)


def update_dart(request):
    user = DriverUser.objects.filter(id=request.user.id).order_by('-id')
    posts = Post.objects.filter(author=user).order_by('-id')
    dict = {}
    for users in user:
        dict['username'] = users.username
        dict['email'] = users.email
        dict['password'] = users.password
        dict['n_user'] = users.pk
        dict['first_name'] = users.first_name

    dict['posts'] = posts
    context_posts = dict
    return render(request, 'user_profile/profile_detai_updatel.html', context_posts)


def update_post(request, pk):
    post = Post.objects.get(pk=pk)

    form = UpdateForm(request.POST, instance=post)
    all_category = Category.objects.all()
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            form.save()
    return render(request, 'user_profile/update.html', {'form': form, 'all_category': all_category, 'post': post})


def update_user(request, pk):
    user = User.objects.get(id=pk)
    print('matrildeklaksdasa')
    print(user)
    form = UserForm(request.POST, instance=user)

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.GET.get('username', None)
            user.save()
            return redirect('post_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'user_profile/profile_detail.html', {'form': form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('myprofile:list')
    context = {
        "object": post
    }
    return render(request, 'user_profile/delete.html', context)
