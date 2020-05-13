from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.c19menu),
    path('c19cadastro',views.c19cadastro_form,name='c19cadastro_novo'),
    path('c19cadastro<int:idcad19>',views.c19cadastro_form,name='c19cadastro_altera'),
    path('c19cadastro_exclui<int:idcad19>',views.c19cadastro_exclui,name='c19cadastro_exclui'),
    path('c19cadastro_list/',views.c19cadastro_list,name='c19cadastro_lista'),

    path('c19teste',views.c19teste_form,name='c19teste_novo'),
    path('c19teste<int:idtst19>',views.c19teste_form,name='c19teste_altera'),
    path('c19teste_exclui<int:idtst19>',views.c19teste_exclui,name='c19teste_exclui'),
    path('c19teste_list/',views.c19teste_list,name='c19teste_lista'),

    path('c19autoaval',views.c19autoaval_form,name='c19autoaval_novo'),
    path('c19autoaval<int:idaut19>',views.c19autoaval_form,name='c19autoaval_altera'),
    path('c19autoaval_exclui<int:idaut19>',views.c19autoaval_exclui,name='c19autoaval_exclui'),
    path('c19autoaval_list/',views.c19autoaval_list,name='c19autoaval_lista'),
]
