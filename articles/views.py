from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Post


def articles_view(request):
	ARTICLES_PER_PAGE = 3

	query = request.GET.get('q')
	if query:
		post_list = Post.published.filter(
			Q(title__icontains=query) |
			Q(content__contains=query) | 
			Q(description__contains=query) |
			Q(author__contains=query)
		).distinct().filter(is_active=True, language='EN')
	else:
		post_list = Post.published.filter(is_active=True, language='EN')

	paginator = Paginator(post_list, ARTICLES_PER_PAGE)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	template = 'articles.html'
	context = {
		'posts': posts,
	}

	return render(request, template, context)

def articles_pl_view(request):
	if settings.DEBUG:
		ARTICLES_PER_PAGE = 3
	else: 
		ARTICLES_PER_PAGE = 9

	query = request.GET.get('q')
	if query:
		post_list = Post.published.filter(
			Q(title__icontains=query) |
			Q(content__contains=query) |
			Q(description__contains=query) |
			Q(author__contains=query)
		).distinct().filter(is_active=True, language='PL')
	else:
		post_list = Post.published.filter(is_active=True, language='PL')

	paginator = Paginator(post_list, ARTICLES_PER_PAGE)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	template = 'articles-pl.html'
	context = {
		'posts': posts,
	}

	return render(request, template, context)

def post_view(request, slug):
	post = get_object_or_404(Post, slug=slug, is_active=True, language='EN')

	try:
		prev_post = post.get_previous_by_publish(is_active=True, language='EN')
	except Post.DoesNotExist:
		prev_post = None
	try:
		next_post = post.get_next_by_publish(is_active=True, language='EN')
	except Post.DoesNotExist:
		next_post = None

	template = 'post.html'
	context = {
		'post': post,
		'prev_post': prev_post,
		'next_post': next_post,
	}

	return render(request, template, context)

def post_pl_view(request, slug):
	post = get_object_or_404(Post, slug=slug, is_active=True, language='PL')
	render_date = False

	try:
		prev_post = post.get_previous_by_publish(is_active=True, language='PL')
	except Post.DoesNotExist:
		prev_post = None
	try:
		next_post = post.get_next_by_publish(is_active=True, language='PL')
	except Post.DoesNotExist:
		next_post = None

	template = 'post-pl.html'
	context = {
		'post': post,
		'prev_post': prev_post,
		'next_post': next_post,
		'render_date': render_date,
	}

	return render(request, template, context)