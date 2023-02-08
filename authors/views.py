from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Biography, Article, Book
from .serializers import AuthorSerializer, BiographySerializer, ArticleSerializer, BookSerializer
# from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView, ListAPIView
# from rest_framework.renderers import JSONRenderer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ['name']


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['name']


class MyAPIView(ViewSet):
    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
