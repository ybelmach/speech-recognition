import uuid

from queries.models import UsersOrm
from queries.database import async_session


def insert_data(id: uuid.UUID, link: str, text: str):
    with async_session() as session:
        user = UsersOrm(id=id, link=link, text=text)
        session.add_all([user, ])
        session.commit()


def update_data(link: str, text: str):
    pass
