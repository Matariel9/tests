from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService

import pytest


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    dir1 = Director(id = 1, name = "Oleg")
    dir2 = Director(id = 2, name = "Artem")

    director_dao.get_all = MagicMock(return_value = [dir1, dir2])
    director_dao.get_one = MagicMock(return_value = dir1)
    director_dao.create = MagicMock(return_value = Director(id=2))
    director_dao.update = MagicMock(return_value = True)
    director_dao.delete = MagicMock()

    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse = True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_all(self):
        all = self.director_service.get_all()
        assert len(all)>0

    def test_get_one(self):
        one = self.director_service.get_one(1)
        assert one is not None
        assert one.id is not None

    def test_create(self):
        create = self.director_service.create(1)
        assert create.id is not None

    def test_delete(self):
        self.director_service.delete(2)

    def test_update(self):
        update = self.director_service.update(Director(id = 2, name = "oogway"))
        assert update
