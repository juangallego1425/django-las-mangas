from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.vias, name="via"),
    path('<int:via_id>/', views.comentario, name='comentario_via'),
    path('lista/', views.listar, name='listar'),

]