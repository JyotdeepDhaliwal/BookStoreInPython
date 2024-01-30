from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from ..models import Book

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/',
        '/api/books/',
        '/api/books/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBook(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)
