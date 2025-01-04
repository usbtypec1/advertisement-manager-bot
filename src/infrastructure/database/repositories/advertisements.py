from sqlalchemy.dialects.sqlite import insert

from infrastructure.database.models.advertisements import Advertisement
from infrastructure.database.repositories.base import DatabaseRepository


class AdvertisementRepository(DatabaseRepository):
    def create(self):
        insert(Advertisement).values()
