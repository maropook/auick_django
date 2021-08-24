from django import forms
from django.shortcuts import render, redirect
from .models import Book
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse, Http404, response
import random
import csv
import urllib.parse
from .forms import BookForm, UploadForm, BookModelForm
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from django.urls import reverse


def index(request):
    return HttpResponse('おはよう世界')


def temp(request):
    context = {
        'msg': 'こんにちは、世界！'

    }
    return render(request, 'main/temp.html', context)

# Bookテーブルに入っているオブジェクトを出力


def list(request):
    books = Book.objects.all()
    return render(request, 'main/list.html', {
        'books': books
    })

# ランダムな値を返す．それがどのくらいか比較する


def iftag(request):
    return render(request, 'main/iftag.html', {
        'random': random.randint(0, 100)
    })

# 真偽地に応じた文字列を出力する


def yesno(request):
    return render(request, 'main/yesno.html', {
        'flag': None
    })

# 最初にtrueとなった値を返す


def firstof(request):
    return render(request, 'main/firstof.html', {
        'a': 'おはよう',
        'b': 'おう',
        'c': 'おは',

    })


def forloop(request):
    return render(request, 'main/forloop.html', {
        'weeks': ['月', '火', '水', '木', '金']
    })


def forempty(request):
    return render(request, 'main/forempty.html', {
        'members': ['鈴木三郎', '佐藤陽子', '山田二郎']
    })


def fortag(request):
    return render(request, 'main/fortag.html', {
    })


def master(request):
    return render(request, 'main/master.html', {
        'msg': 'こんちゃす'
    })


def static(request):
    return render(request, 'main/static.html', {

    })


def filter(request):
    books = Book.objects.filter(publisher='照英社')
    return render(request, 'main/book_list.html', {
        'books': books
    })


def exclude(request):
    books = Book.objects.exclude(publisher='照英社')
    return render(request, 'main/book_list.html', {
        'books': books
    })


def get(request):
    book = Book.objects.get(pk=1)
    return render(request, 'main/book_detail.html', {
        'book': book
    })


def rel(request):
    return render(request, 'main/rel.html', {
        'book': Book.objects.get(pk=1)
    })


def rel2(request):
    return render(request, 'main/rel2.html', {
        'books': Book.objects.all()
    })


def route_param(request, id=1):
    return HttpResponse(f'id値:{id}')

# http://localhost:8000/req_query?id=3&ei=UTF-8このようにアクセスする


def req_query(request):
    return HttpResponse(f'id値:{request.GET["id"]}')


def req_header(request):
    return HttpResponse(f'Use-Agent:{request.headers["User-Agent"]}')


def req_redirect(request):
    book = Book.objects.get(pk=1)
    # return redirect('req_header')
    return redirect(book)
    # nameパラメータを指定
    # return redirect('route_param',id=10)パラメータに値を引き渡すこともできる


def details(request, id):
    return HttpResponse(f'id値：{id}')


def res_notfound(request):
    try:
        book = Book.objects.get(pk=108)
    except Book.DoesNotExist:
        raise Http404('指定の書籍情報が存在しません')
    return render(request, 'main/book_detail.html', {
        'book': book
    })


def res_header(request):
    response = HttpResponse('<message>Hello,world!!</message>',
                            content_type='text/xml')
    response['Content-Disposition'] = 'attachment;filename="hoge.xml"'
    return response


def res_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="data."csv"'
    writer = csv.writer(response)
    writer.writerows([
        ['tyamada', '山田太郎', '30']
    ])
    return response


def json(request):
    return response.JsonResponse(['Python', 'Ruby'], safe=False)


def setcookie(request):
    response = HttpResponse(render(request, 'main/setcookie.html'))
    response.set_cookie('app_title',
                        urllib.parse.quote('速習Django'), 60 * 60 * 24 * 30, samesite='Strict')
    # return response
    return response


def getcookie(request):
    app_title = urllib.parse.unquote(request.COOKIES['app_title']) \
        if 'app_title' in request.COOKIES else '－'
    return render(request, 'main/getcookie.html', {
        'app_title': app_title
    })


def setsession(request):
    request.session['app_title'] = 'ああ'
    return HttpResponse('セッションを保存しました')


def getsession(request):
    title = request.session['app_title'] \
        if 'app_title' in request.session else '-'
    return HttpResponse(title)


class MyTempView(TemplateView):
    template_name = 'main/temp.html'
    # テンプレートのパス

    def get_context_data(self, **kwargs):
        # ビュー変数を取得
        context = super().get_context_data(**kwargs)
        context['msg'] = 'こんにちは世界'
        return context

# def temp(request):
#     context = {
#         'msg': 'こんにちは、世界！'

#     }
#     return render(request, 'main/temp.html', context)


def form_input(request):
    form = BookForm()
    return render(request, 'main/form_input.html', {
        'form': form
    })


@require_POST
def form_process(request):
    form = BookForm(request.POST)
    if form.is_valid():
        return render(request, 'main/form_process.html', {
            'form': form
        })
    else:
        return render(request, 'main/form_input.html', {
            'form': form
        })


def upload_input(request):
    form = UploadForm()
    return render(request, 'main/upload_input.html', {
        'form': form
    })


@require_POST
def upload_process(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        file = form.cleaned_data['body']
        with open(file.name, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)
        return HttpResponse(f'{file.name}のアップロードに成功')
    return HttpResponse('アップロードに失敗')


def crud_new(request):
    form = BookModelForm()
    return render(request, 'main/crud_new.html', {
        'form': form
    })


@require_POST
def crud_create(request):
    obj = Book()
    form = BookModelForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             'データの保存に成功しました')
        return redirect('crud_new')
    else:
        return render(request, 'main/crud_new.html', {
            'form': form
        })


def crud_edit(request, id):
    obj = Book.objects.get(pk=id)
    form = BookModelForm(instance=obj)
    return render(request, 'main/crud_edit.html', {
        'id': id,
        'form': form
    })


@require_POST
def crud_update(request, id):
    obj = Book.objects.get(pk=id)
    form = BookModelForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        messages.set_level(request, messages.WARNING)
        messages.success(request, 'データの更新に成功しました。')
        return redirect(reverse('crud_edit', kwargs={'id': id}))
    else:
        return render(request, 'main/crud_edit.html', {
            'id': id,
            'form': form
        })


def crud_show(request, id):
    obj = Book.objects.get(pk=id)
    form = BookModelForm(instance=obj)
    return render(request, 'main/crud_show.html', {
        'id': id,
        'form': form
    })


@require_POST
def crud_delete(request, id):
    obj = Book.objects.get(pk=id)
    obj.delete()
    messages.success(request, 'データの削除に成功')
    return redirect(reverse('list'))
