from django.shortcuts import get_object_or_404, render, redirect
from . models import Group, Post, Follow
from django.contrib.auth.decorators import login_required
from . forms import PostForm, CommentForm
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView


User = get_user_model()

POST_PER_PAGE = 3


def paginator(request, group):
    paginator = Paginator(group, POST_PER_PAGE)
    page_numder = request.GET.get('page')
    page_obj = paginator.get_page(page_numder)
    return page_obj


def index(request):
    posts = Post.objects.select_related("group", "author")
    page_obj = paginator(request, posts)
    context = {"posts": posts,
               'page_obj': page_obj}
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related("author")
    page_obj = paginator(request, posts)
    context = {"posts": posts,
               "group": group,
               "page_obj": page_obj}
    return render(request, 'posts/group_list.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    context = {'form': form}
    if form.is_valid():
        post = form.save(commit=False)
        post.author_id = request.user.id
        post.save()
        return redirect('posts:profile', request.user.username)
    return render(request, 'posts/post_create.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.select_related('group')
    page_obj = paginator(request, posts)
    posts_count = posts.count()
    following = (
        request.user.is_authenticated and author.followed.filter(
            user=request.user,
            author=author).exists() and request.user.follower.filter(
                user=request.user, author=author).exists())
    context = {'posts': posts,
               'author': author,
               'posts_count': posts_count,
               'page_obj': page_obj,
               'following': following}
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    posts = post.author.posts
    posts_count = posts.count()
    form = CommentForm()
    comments = post.comments.all()
    context = {'post': post,
               'posts_count': posts_count,
               'comments': comments,
               'form': form}
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(
        request.POST or None,
        instance=post,
        files=request.FILES or None)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id=post_id)
    context = {'post': post,
               'form': form,
               'is_edit': True}
    if form.is_valid():
        post = form.save()
        return redirect('posts:post_detail', post_id=post_id)
    return render(request, 'posts/post_create.html', context)


@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


@login_required
def follow(request, username):
    author = get_object_or_404(User, username=username)
    if request.user != author:
        Follow.objects.get_or_create(author=author, user=request.user)
    return redirect('posts:profile', username=username)


@login_required
def unfollow(request, username):
    author = get_object_or_404(User, username=username)
    Follow.objects.filter(author=author, user=request.user).delete()
    return redirect('posts:profile', username=username)


@login_required
def favourite(request):
    posts = Post.objects.filter(author__followed__user=request.user)
    page_obj = paginator(request, posts)
    context = {'page_obj': page_obj}
    return render(request, 'posts/favourite.html', context)


class SearchResultsView(ListView):
    model = Post
    template_name = 'posts/search_results.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query', '').strip()
        if not query:
            return Post.objects.none()
        return Post.objects.select_related('group', 'author').filter(
            Q(text__icontains=query)
            | Q(author__username__icontains=query)
            | Q(group__title__icontains=query)
            | Q(title__icontains=query)
        ).distinct().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get('query', '')
        return context
