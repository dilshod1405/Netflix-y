from django.test import TestCase, Client

from index.models import Movie, Actor


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.movie = Movie.objects.create(name='Charlie Chaplin', imdb=5, year=1961, genre='Funny')
        self.actor = Actor.objects.create(name='Charlie', birthdate='1921-11-01', gender='M')
        self.movie.actor.add(self.actor)
        self.movie_2 = Movie.objects.all()
        self.movie_3 = Movie.objects.create(year=2019, imdb=5, name='Kremen', genre='Funny')
        self.actor_3 = Actor.objects.create(name='Maksim', birthdate='1986-07-08', gender='M')
        self.movie_4 = Movie.objects.create(year=2019, imdb=5, name='Баталён-2', genre='Funny')
        self.actor_4 = Actor.objects.create(name='Maksim', birthdate='1986-07-08', gender='M')
        self.movie_5 = Movie.objects.create(year=2019, imdb=5, name='Баталён-3', genre='Funny')
        self.actor_5 = Actor.objects.create(name='Maksim', birthdate='1986-07-08', gender='M')
        self.movie.actor.add(self.actor)

    def test_get_list(self):
        response = self.client.get('/movies/')
        data = response.data
        print(response)
        self.assertEquals(len(data), 4)
        self.assertEqual(data[0]['name'], 'Charlie Chaplin')

    def test_search(self):
        response = self.client.get('/movies/?search=Kremen')
        data = response.data
        print(response)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)

    def test_ordering(self):
        response = self.client.get('/movies/?ordering=imdb')
        data = response.data
        print(response)

        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(data), 4)
        self.assertEqual(data[0]['imdb'], 1)
