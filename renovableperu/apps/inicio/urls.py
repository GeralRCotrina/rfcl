
from django.urls import path, re_path
from apps.inicio import views
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required


urlpatterns = [
	re_path(r'^pres/$',views.presentacion,name='pres'),
	re_path(r'^cuerpo/$', login_required(views.index),name='cuerpo'),

	re_path(r'^por_reg/?/$',login_required(views.RegPortafolio),name='por_reg'),
	re_path(r'^guar_comn/?/$',views.guardar_comentario,name='guar_comn'),
	re_path(r'^logon/?/$',views.logon,name='logon'),
	re_path(r'^$',views.presentacion,name='pr'),
	re_path(r'^accounts/login/$',views.presentacion,name='accounts/login/'),
	re_path(r'^logout$',logout_then_login,name='logout'),

	re_path(r'^por_reg1/$',login_required(views.PorCreate.as_view()),name='por_reg1'),
	re_path(r'^por_lis/$',login_required(views.PorList.as_view()),name='por_lis'),
	re_path(r'^por_edi/(?P<pk>\d+)/$',login_required(views.PorUpdate.as_view()),name='por_edi'),
	re_path(r'^por_eli/(?P<pk>\d+)/$',login_required(views.PorDelete.as_view()),name='por_eli'),


	re_path(r'^panel/$',login_required(views.Panel.as_view()),name='panel'),


	re_path(r'^a/$',login_required(views.PorList.as_view()),name='a'),




	re_path(r'^p_prin/$',login_required(views.PanelPrincipal.as_view()),name='p_prin'),
	re_path(r'^t_prin/$',login_required(views.Tienda.as_view()),name='t_prin'),
	re_path(r'^t_prod/$',login_required(views.Producto.as_view()),name='t_prod'),
	re_path(r'^t_car/$',login_required(views.Carrito.as_view()),name='t_car'),
] 


