from django.shortcuts import render, redirect, HttpResponse
from apps.inicio.models import AuthUser, Mensajes, Portafolio
from django.views.generic import View

from django.views.generic import ListView, CreateView,UpdateView,DeleteView, TemplateView, View
from apps.inicio.forms import PortafolioForm
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login


import datetime
# Create your views here.


 
"""
class ActUsuario(View):

	def get(self, request, *args, **kwargs):
		dicc={}
		dicc['userr']= 'bacío'
		return render(request,'p_act_usu.html',dicc)

	def post(self, request, *args, **kwargs):
		dicc={}
		usuario = self.request.POST.get('usuario')
		dicc['userr']= usuario
		if AuthUser.objects.filter(username__exact=usuario).exists():
			print('__________No hay nueva contraseña aún..')
			u=AuthUser.objects.get(username__exact=usuario)
			dicc['passs']= u.password
			dicc['usuario']= usuario
			dicc['msj']= 'nda'
		else:
			dicc['msj']= 'nusr'
		return render(request,'p_act_usu.html',dicc)
"""



class Panel(View):

	def get(self, request, *args, **kwargs):
		dicc={}
		dicc['msj']= 'Llegó'
		return render(request,'cuerpo.html',dicc)

	def post(self, request, *args, **kwargs):
		dicc={}
		usuario = self.request.POST.get('usuario')
		dicc['userr']= usuario
		if AuthUser.objects.filter(username__exact=usuario).exists():
			print('__________No hay nueva contraseña aún..')
			u=AuthUser.objects.get(username__exact=usuario)
			dicc['passs']= u.password
			dicc['usuario']= usuario
			dicc['msj']= 'nda'
		else:
			dicc['msj']= 'nusr'
		return render(request,'cuerpo.html',dicc)



class PanelPrincipal(View):

	def get(self, request, *args, **kwargs):
		dicc={}
		dicc['msj']= 'Llegó'
		return render(request,'panel/p_prin.html',dicc)

	


class Tienda(View):

	def get(self, request, *args, **kwargs):
		dicc={}
		dicc['msj']= 'Llegó'
		return render(request,'tienda/t_prin.html',dicc)


class Producto(View):

	def get(self, request, *args, **kwargs):
		dicc={}
		dicc['msj']= 'Llegó'
		return render(request,'tienda/t_prod.html',dicc)

class Carrito(View):

	def get(self, request, *args, **kwargs):
		dicc={}
		dicc['msj']= 'Llegó'
		return render(request,'tienda/t_car.html',dicc)
		

class PorCreate(CreateView):
	model=Portafolio
	form_class=PortafolioForm
	template_name='por_reg.html'
	success_url=reverse_lazy('pres')

class PorList(ListView):
	model=Portafolio
	template_name='p_noticia_lis.html'
	paginate_by=9

class PorUpdate(UpdateView):
	model=Portafolio
	form_class=PortafolioForm
	template_name='p_noticia_reg.html'
	success_url=reverse_lazy('p_noticia_lis') 

class PorDelete(DeleteView):
	model=Portafolio
	form_class=PortafolioForm
	template_name='p_noticia_eli.html'
	success_url=reverse_lazy('p_noticia_lis')





def index(request):
	return render(request,'index.html')

def presentacion(request):
	return render(request,'prs.html')


def guardar_comentario(request):
	dicc={}
	dicc['msj1']="OK"
	if request.method == 'GET':
		print('  >> GET')
		name=request.GET['nam']
		email=request.GET['email']
		phone=request.GET['phone']
		message=request.GET['message']
		print('  >> n: '+name+'  >> @: '+email+'  >> t: '+phone+'  >> m: '+message)

		tim = datetime.datetime.now()
		userr=AuthUser(first_name=name,email=email,celular=phone,is_superuser=0,is_staff=0,is_active=1,date_joined=tim)
		userr.save()

		msj_db = Mensajes(id_user=list(AuthUser.objects.all())[-1],fecha=tim,mensaje=message)
		msj_db.save()

		return HttpResponse(dicc)
	else:
		print('  >> POST')
		return HttpResponse(dicc)
	return HttpResponse(dicc)

 

def logon(request):
	print("  > p01")
	if request.method == 'GET':
		username = request.GET['us']
		password = request.GET['ps']
		print("  >> us:"+username)
		print("  >> ps:"+password)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			print("  >>us E")
			login(request, user)
			print("  >> login success")
			return HttpResponse({'msj':'ok'})
		else:
			print("  >> usre no E/")
			return HttpResponse({'msj':'Err'})



def RegPortafolio(request):

	if request.method == 'GET':
		p_tit =  request.GET['p_tit']
		p_titu =  request.GET['p_titu']
		p_lug =  request.GET['p_lug']
		p_desc =request.GET['p_desc']	
		p_cal = request.GET['p_cal']	
		p_cat =request.GET['p_cat']
		p_fec = request.GET['p_fec']
		p_fot = request.GET['p_fot']
		
		port = Portafolio(titulo_por=p_tit,titular_p=p_titu,descripcion_por=p_desc,imagen_por=p_fot,lugar_por=p_lug,fecha_por=p_fec,calificacion_por=p_cal)

		port.save()

		print("  >>> success full")

		return HttpResponse({'msj':'ok'})







