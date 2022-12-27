from unittest.mock import MagicMock

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService

import pytest


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    gen1 = Genre(id = 1, name = "Oleg")
    gen2 = Genre(id = 2, name = "Artem")

    genre_dao.get_all = MagicMock(return_value = [gen1, gen2])
    genre_dao.get_one = MagicMock(return_value = gen1)
    genre_dao.create = MagicMock(return_value = Genre(id=2))
    genre_dao.update = MagicMock(return_value = True)
    genre_dao.delete = MagicMock()

    return genre_dao

class TestGenreService:
    @pytest.fixture(autouse = True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_all(self):
        all = self.genre_service.get_all()
        assert len(all)>0

    def test_get_one(self):
        one = self.genre_service.get_one(1)
        assert one is not None
        assert one.id is not None

    def test_create(self):
        create = self.genre_service.create(1)
        assert create.id is not None

    def test_delete(self):
        self.genre_service.delete(2)

    def test_update(self):
        update = self.genre_service.update(Genre(id = 2, name = "napkin"))
        assert update
