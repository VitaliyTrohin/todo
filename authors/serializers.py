from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Biography, Article, Book
from rest_framework import serializers


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ['name'] # выбрать все, кроме 'name'


class BiographySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class ArticleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class BookSerializerBase(serializers.ModelSerializer):
    class Meta:
          model = Book
          fields = '__all__'     


class BookSerializer(HyperlinkedModelSerializer):
    # author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'

"""
author1 = Author.objects.create(name='Грин', birthday_year=1880)
serializer = AuthorSerializer(author1)
print(serializer.data) # {'id': 17, 'name': 'Грин', 'birthday_year': 1880}

biography = Biography.objects.create(text='Некоторая биография', author=author1)
serializer = BiographySerializer(biography)
print(serializer.data) # {'text': 'Некоторая биография', 'author': 17}

article = Article.objects.create(name='Некоторая статья', author=author1)
serializer = ArticleSerializer(article)
print(serializer.data) # {'id': 8, 'author': OrderedDict([('id', 17), ('name', 'Грин'), ('birthday_year', 1880)])}

author2 = Author.objects.create(name='Пушкин', birthday_year=1799)
book = Book.objects.create(name='Некоторая книга')
book.authors.add(author1)
book.authors.add(author2)
book.save()
serializer = BookSerializer(book)
print(serializer.data) # {'id': 9, 'authors': ['Грин', 'Пушкин'], 'name': 'Некоторая книга'}        
"""