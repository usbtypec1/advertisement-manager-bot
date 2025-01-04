from sqlalchemy.dialects.sqlite import insert

from infrastructure.database.models.advertisements import Advertisement
from infrastructure.database.dao.base import DatabaseDAO


class AdvertisementDAO(DatabaseDAO):
    def create(self):
        insert(Advertisement).values()
