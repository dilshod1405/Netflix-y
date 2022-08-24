from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from index.models import Movie, Actor, Comment
from index.serializers import MovieSerializer, ActorSerializer, CommentSerial


class CommentViewset(ReadOnlyModelViewSet):
    serializer_class = CommentSerial
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(user_id=self.request.user)


class ComentAPI_create(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer = CommentSerial

    def post(self, request):
        serializer = CommentSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors.error, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerial(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response('Successfully deleted')


# class ComentAPI_edit(APIView):
#    permission_classes = (IsAuthenticated,)
#    authentication_classes = (TokenAuthentication,)
#    serializer = CommentSerial

#   def get(self, request):
#      serializer = Comment.objects.all()
#     return HttpResponse(serializer)


# class ComentAPI_delete(APIView):
#   permission_classes = (IsAuthenticated,)
#  authentication_classes = (TokenAuthentication,)
# serializer = CommentSerial

# def delete(self, request, pk):
#   comment = Comment.objects.filter(movie_id__comment=pk).delete()
#  return Response('Successfully deleted')


class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['imdb']
    search_fields = ['name', 'year']
    filterset_fields = ['genre']

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['PATCH'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actors = Actor.objects.get(id=request.data.get('id'))
        movie.actor.add(actors)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['PATCH'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actors = Actor.objects.get(id=request.data.get('id'))
        movie.actor.remove(actors)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActorViewSet(MovieViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


def MovieapiView(request):
    a = Movie.objects.all()
    return render(request, 'index/index.html', {
        'a': a,
    })


def ActorapiView(request):
    b = Actor.objects.all()
    return render(request, 'index/actors.html', {
        'b': b,
    })
