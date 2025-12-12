from django.urls import path
from . import views
app_name ='programas'

urlpatterns = [
    path('', views.main, name='main'),
    path('programas/', views.programas, name='programas'),
    path('programas/details/<int:id>', views.details, name='details'),
    path('programas/agregar/', views.ProgramaCreateView.as_view(), name='agregar_programa'),
    path('programas/editar/<int:programa_id>', views.ProgramaUpdateView.as_view(), name='editar_programa'),
    path('programas/eliminar/<int:programa_id>', views.ProgramaDeleteView.as_view(), name='eliminar_programa'),
    
]