from rest_framework import serializers
from .models import Movie, Actor, Comment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'year', 'genre', 'actor', 'id', 'imdb')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'birthdate', 'gender', 'id',)

    def validate_birthdate(self, value):
        if value.year < 1950:
            raise 'Date is un correctly'
        print('correctly')
        return value


class CommentSerial(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('movie_id', 'text', 'created_date', 'user_id')
