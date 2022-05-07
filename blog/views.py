from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import View

from django.http import HttpResponse #

from .models import Post, Section
from .utils import *
from .forms import SectionForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q



def posts_list(request):
    search_query = request.GET.get('search','')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context  = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'blog/index.html', context = context)

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'



class PostCreate(LoginRequiredMixin, ObjectCreateMIxin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = False

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = False

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = False

class SectionDetail(ObjectDetailMixin, View):
    model = Section
    template = 'blog/section_detail.html'

class SectionCreate(LoginRequiredMixin, ObjectCreateMIxin, View):
    model_form = SectionForm
    template = 'blog/section_create.html'
    raise_exception = False

class SectionUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Section
    model_form = SectionForm
    template = 'blog/section_update_form.html'
    raise_exception = False

class SectionDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Section
    template = 'blog/section_delete_form.html'
    redirect_url = 'sections_list_url'
    raise_exception = False

def sections_list(request):
    sections = Section.objects.all()
    return render(request, 'blog/sections_list.html', context={'sections': sections})
