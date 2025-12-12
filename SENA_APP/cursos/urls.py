from django.urls import path
from . import views

# Namespace para evitar conflictos con otras apps
app_name = 'cursos'

urlpatterns = [
    path('', views.main, name='main'), # Namespace para evitar conflictos con otras apps
    path('cursos/', views.cursos, name='lista_cursos'),
    path('cursos/datails/<int:curso_id>/', views.details, name='details'),
    path('cursos/agregar/', views.CursoCreateView.as_view(), name='agregar_curso'),
    path('cursos/editar/<int:curso_id>', views.CursoUpdateView.as_view(), name='editar_curso'),
    path('cursos/eliminar/<int:curso_id>', views.CursoDeleteView.as_view(), name='eliminar_curso'),
]