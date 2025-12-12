from django.urls import path
from . import views
app_name ='instructores'
urlpatterns = [
    path('', views.main, name='main'),
    path('instructores/', views.instructores, name='instructores'),
    path('instructores/details/<int:id>', views.details, name='details'),
    path(' instructores/agregar/', views.InstructorCreateView.as_view(), name='agregar_instructor'),
    path('instructores/editar/<int:Instructor_id>', views.InstructorUpdateView.as_view(), name='editar_instructor'),
    path('instructores/eliminar/<int:Instructor_id>', views.InstructorDeleteView.as_view(), name='eliminar_instructor'),
    
]