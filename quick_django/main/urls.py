from django.urls import path
from django.urls.resolvers import URLPattern

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('iftag', views.iftag, name='iftag'),
    path('yesno', views.yesno, name='yesno'),
    path('firstof', views.firstof, name='firstof'),
    path('forloop', views.forloop, name='forloop'),
    path('forempty', views.forempty, name='forempty'),
    path('fortag', views.fortag, name='fortag'),
    path('master', views.master, name='master'),
    path('static', views.static, name='static'),
    path('filter', views.filter, name='filter'),
    path('exclude', views.exclude, name='exclude'),
    path('get', views.get, name='get'),
    path('rel', views.rel, name='rel'),
    path('rel2', views.rel2, name='rel2'),
    path('route_param/<int:id>', views.route_param, name='route_param'),
    path('route_param', views.route_param, name='route_param'),
    path('req_query', views.req_query, name='req_query'),
    path('req_header', views.req_header, name='req_header'),
    path('req_redirect', views.req_redirect, name='req_redirect'),
    path('details/<int:id>', views.details, name='details'),
    path('res_notfound', views.res_notfound, name='res_notfound'),
    path('res_header', views.res_header, name='res_header'),
    path('res_csv', views.res_csv, name='res_csv'),
    path('setcookie', views.setcookie, name='setcookie'),
    path('getcookie', views.getcookie, name='getcookie'),
    path('setsession', views.setsession, name='setsession'),
    path('getsession', views.getsession, name='getsession'),

    # path('temp', views.temp, name='temp'),
    path('temp_view', views.MyTempView.as_view(), name='temp_View'),
    path('form_input', views.form_input, name='form_input'),
    path('form_process', views.form_process, name='form_process'),
    path('upload_input', views.upload_input, name='upload_input'),
    path('upload_process', views.upload_process, name='upload_process'),
    path('crud_new', views.crud_new, name='crud_new'),
    path('crud_create', views.crud_create, name='crud_create'),
    path('crud_edit/<int:id>', views.crud_edit, name='crud_edit'),
    path('crud_update/<int:id>', views.crud_update, name='crud_update'),
    path('crud_show/<int:id>', views.crud_show, name='crud_show'),
    path('crud_delete/<int:id>', views.crud_delete, name='crud_delete'),

]
