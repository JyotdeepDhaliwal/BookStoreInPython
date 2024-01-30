from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
