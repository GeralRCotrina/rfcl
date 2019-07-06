from django import forms
from apps.inicio.models import Portafolio


class PortafolioForm(forms.ModelForm):

	class Meta:
		model = Portafolio

		fields = ['ip_por','titulo_por','titular_p','descripcion_por',
			'imagen_por','lugar_por','fecha_por','calificacion_por',
		]

		labels = {
			'titulo_por':'Portafolio 1° título',
			'titular_p':'2° título',
			'descripcion_por':'Descripción del trabajo',
			'imagen_por':'Seleciona una imagen',
			'lugar_por':'El lugar donde se relizó',
			'calificacion_por':'Dale una calificación (0-10)',
			'fecha_por':'Fecha',
		}

		widgets={
			'titulo_por':forms.TextInput(attrs={'class':'form-control'}),
			'titular_p':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion_por':forms.Textarea(attrs={'class':'form-control','rows':'2'}),
			'imagen_por':forms.FileInput(attrs={'class':'btn-block'}),
			'lugar_por':forms.TextInput(attrs={'class':'form-control'}),
			'calificacion_por':forms.NumberInput(attrs={'type':'range','step':'0.5','max':'9','min':'0','class':'form-control'}),
			'fecha_por':forms.DateInput(attrs={'class':'form-control'}),
		}



"""
'calificacion_por':forms.InegerField(attrs={'class':'form-control'}),
class Portafolio(models.Model):
    ip_por = models.AutoField(primary_key=True)
    titulo_por = models.CharField(max_length=70)
    titular_p = models.CharField(max_length=130)
    descripcion_por = models.CharField(max_length=500)
    imagen_por = models.ImageField(upload_to='media')
    lugar_por = models.CharField(max_length=100)
    fecha_por = models.DateTimeField()
    calificacion_por = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'portafolio'



class PersonaForm(forms.ModelForm):

	class Meta:
		model = DatosPersonales

		fields = ['id_datos_personales','dni','sexo',
		    'alias','fecha_nacimiento','telefono','celular','foto','id_auth_user',
		]

		labels = {
			'dni':'DNI',
			'alias':'alias',
			'sexo':'Sexo',
			'fecha_nacimiento':'fecha nacimiento',
			'telefono':'telefono',
			'celular':'Movil',
			'foto':'foto',
			'id_auth_user':'seleccione el usuario',
		}

		widgets={
			'dni':forms.TextInput(attrs={'class':'form-control'}),
			'alias':forms.TextInput(attrs={'class':'form-control'}),
			'sexo':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control','type':'date'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'celular':forms.TextInput(attrs={'class':'form-control'}),
			'foto':forms.FileInput(attrs={'class':'btn-block'}),
			'id_auth_user':forms.Select(attrs={'class':'form-control'}),
		}



"""