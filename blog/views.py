from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse, get_object_or_404
from django.template import Context,Template
from django.shortcuts import render

# Create your views here.

from blog.models import *
from . import models

def index(request):
    aritcle = get_object_or_404(Aritcle)
    # aritcle = models.Aritcle.browse_num
    num = aritcle.browse_num
    num = num+1
    aritcle.browse_num=num
    aritcle.save()

    context = {}
    aritcle_list = Aritcle.objects.all()
    context['aritcle_list'] = aritcle_list
    index_page = render(request, 'index.html', context)
    # render第三个参数是后台传送到前端的数据
    # return render(request, 'blog/index.html', context={'post_list': post_list})
    return index_page

def aritcle_page(request,aritcle_id):
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

