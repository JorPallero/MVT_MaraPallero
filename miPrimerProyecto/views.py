from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader
import random

from miPrimerApp.models import Familiar

def crear_familiar(request, nombre, apellido, parentesco):
    
    familiar = Familiar(nombre=nombre,apellido=apellido,edad=random.randrange(1,99),fecha_creacion_registro=datetime.now(),parentesco=parentesco)
    familiar.save()
    
    
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({'familiar':familiar})
  
    return HttpResponse(template_renderizado)


def mostrar_familiares(request):
    
    familiares = Familiar.objects.all()
    
    template = loader.get_template('mostrar_familiares.html')
    template_renderizado = template.render({'familiares':familiares})
    
    return HttpResponse(template_renderizado)
