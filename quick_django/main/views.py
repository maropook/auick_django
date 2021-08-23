from django.shortcuts import render
from .models import Book
# Create your views here.
from django.http import HttpResponse
import random


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
