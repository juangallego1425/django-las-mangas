from django.urls import path


from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.anuncios, name='anuncios'),
    path('<int:anuncio_id>/', views.detalle_anuncio, name='detalle_anuncio'),
  
]