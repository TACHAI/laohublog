from django.shortcuts import render,HttpResponse, get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import *
from . import models

def index(request):
    context = {}
    # 取得全部文章放放到aritcle_list
    aritcle_list = Aritcle.objects.all()
    paginator = Paginator(aritcle_list, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    context['aritcle_list'] = aritcle_list
    index_page = render(request, 'index.html', context)
    # render第三个参数是后台传送到前端的数据
    # return render(request, 'blog/index.html', context={'post_list': post_list})
    return index_page

def aritcle_page(request,aritcle_id):
    aritcle = get_object_or_404(Aritcle,pk=aritcle_id)
    # aritcle = models.Aritcle.browse_num
    num = aritcle.browse_num
    num = num + 1
    aritcle.browse_num = num
    aritcle.save()
    context={}
    # aritcle=Aritcle.objects.all()
    aritcle=models.Aritcle.objects.get(pk=aritcle_id)
    context['aritcle']=aritcle
    return render(request,'aritcle_page.html',context)
# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     num = post.browse_num
#     num += 1
#     post.browse_num = num
#     post.save()
#  class index(Listview):
#
#      model = Aritcle


