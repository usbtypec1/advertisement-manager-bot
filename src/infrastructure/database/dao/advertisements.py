from sqlalchemy.dialects.sqlite import insert

from infrastructure.database.dao.base import DatabaseDAO
from infrastructure.database.models.advertisements import Advertisement


class AdvertisementDAO(DatabaseDAO):
    def create(self):
        insert(Advertisement).values()
