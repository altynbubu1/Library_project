from django.shortcuts import render
from rest_framework import viewsets, status, generics
from .permissions import IsAuthorOrReadOnly
from api.models import Book, LibUser, RentBook, BookCategory
from api.serializers import BooksSerializer, LibUserSerializer, RentBookSerializer, BookCategorySerializer
from rest_framework.response import Response

# class BooksViewSet(viewsets.ModelViewSet):
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return BookSerializer
#         elif self.action == 'create':
#             return CreateBookSerializer  # Use a different serializer for creating books
#         # Add more conditions for other actions as needed
#         return super().get_serializer_class()
#
#     def list(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = CreateBookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookListView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


# post
class BookCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


# get and post
class BookListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


# get
class BookRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookUpdateRetrieveView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookDestroyView(generics.DestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

#---------------------


class LibUserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer


class LibUserListView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer


# post
class LibUserCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer


# get and post
class LibUserListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer


# get
class LibUserRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer


# Put
class LibUserUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer


# get and put
class LibUserUpdateRetrieveView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer


# Delete
class LibUserDestroyView(generics.DestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer

#---------------


class RentBookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer


class RentBookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer


class RentBookListView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer

# post
class RentBookCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer

# get and post
class RentBookListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer

# get
class RentBookRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer


# Put
class RentBookUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer


# get and put
class RentBookUpdateRetrieveView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer


# Delete
class RentBookDestroyView(generics.DestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer

# ------------------
class BookCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


class BookCategoryListView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# post
class BookcategoryCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# get and post
class BookCategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# get
class BookCategoryRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# Put
class BookCategoryUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# get and put
class BookCategoryUpdateRetrieveView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# Delete
class BookCategoryDestroyView(generics.DestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# CRUD
# CREATE READ UPDATE DELETE
