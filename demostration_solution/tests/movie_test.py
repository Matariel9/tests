from unittest.mock import MagicMock

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService

import pytest


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    mov1 = Movie(id = 1, title = "alpha fish", description = "double fish", trailer = "triple fish", year = 2000, rating = 10, genre_id = 1, genre = "quadruple fish", director_id = 1, director = "penta fish")
    mov2 = Movie(id = 2, title = "omega fish", description = "double fish", trailer = "triple fish", year = 2000, rating = 10, genre_id = 1, genre = "quadruple fish", director_id = 1, director = "penta fish")

    movie_dao.get_all = MagicMock(return_value = [mov1, mov2])
    movie_dao.get_one = MagicMock(return_value = mov1)
    movie_dao.create = MagicMock(return_value = Movie(id=2))
    movie_dao.update = MagicMock(return_value = True)
    movie_dao.delete = MagicMock()

    return movie_dao

class TestMovieService:
    @pytest.fixture(autouse = True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_all(self):
        all = self.movie_service.get_all()
        assert len(all)>0

    def test_get_one(self):
        one = self.movie_service.get_one(1)
        assert one is not None
        assert one.id is not None

    def test_create(self):
        create = self.movie_service.create(1)
        assert create.id is not None

    def test_delete(self):
        self.movie_service.delete(2)

    def test_update(self):
        update = self.movie_service.update(Movie(id = 2, title = "omega fish", description = "double fish", trailer = "triple fish", year = 2000, rating = 10, genre_id = 1, genre = "quadruple fish", director_id = 1, director = "penta fish"))
        assert update
