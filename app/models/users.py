from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.helper.model import Base, id_key


class User(Base):
    __tablename__ = 'sys_user'
    id: Mapped[id_key] = mapped_column(init=False)
    username: Mapped[str] = mapped_column(String(32), init=False, unique=True)

    def __str__(self) -> str:
        return f'id : {id} - {self.username}'

    def __repr__(self) -> str:
        return f'<User : id: {id} : {self.username}>'
