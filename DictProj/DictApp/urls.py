from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='client-home'),
    path('source/', views.source, name='client-source'),
    path('create_word/', views.create_word, name='create-word'),
    path('update_word/<int:pk>', views.update_word, name='update-word'),
    path('delete_word/<int:pk>', views.delete_word, name='delete-word')
]