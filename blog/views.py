from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    #template_name = 'blog/post_list.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
# def index(request):
#
#     # 데이터베이스에 쿼리를 날려 원하는 레코드를 가져올 수 있음.
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post' : post,
        }
    )