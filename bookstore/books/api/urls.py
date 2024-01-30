from django.urls import path
from .views import getRoutes, getBooks, getBook

urlpatterns = [
    path('', getRoutes, name='api-routes'),
    path('books/', getBooks, name='books'),
    path('books/<int:id>/', getBook, name='book'),
]
