from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.vias, name="via"),
    path('<int:via_id>/', views.comentario, name='comentario_via'),
    path('comentario_via/', views.listar, name='listar'),

]