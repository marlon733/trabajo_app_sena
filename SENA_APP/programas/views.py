
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from .models import Programa
from .forms import ProgramaForm
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

def programas(request):
  myprogramas = Programa.objects.all()
  template = loader.get_template('all_programas.html')
  context = {
    'myprogramas': myprogramas,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  myprograma = Programa.objects.get(id=id)
  template = loader.get_template('details_programas.html')
  context = {
    'myprograma': myprograma,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
class ProgramaCreateView(generic.CreateView):
    """Vista para crear un nuevo programa"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'agregar_programa.html'
    success_url = reverse_lazy('programas:programas')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el programa"""
        messages.success(
            self.request,
            f'El programa {form.instance.get_full_name()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - programa
class ProgramaUpdateView(generic.UpdateView):
    """Vista para actualizar un programa existente"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    success_url = reverse_lazy('programas:programas')
    pk_url_kwarg = 'programa_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El programa {form.instance.get_full_name()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - programa
class ProgramaDeleteView(generic.DeleteView):
    """Vista para eliminar un programa"""
    model = Programa
    template_name = 'eliminar_programa.html'
    success_url = reverse_lazy('programas:programas')
    pk_url_kwarg = 'programa_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        programa = self.get_object()
        messages.success(
            request,
            f'El programa {programa.get_full_name()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)
# Create your views here.
