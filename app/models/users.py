from enum import Enum
from sqlalchemy import BigInteger, Boolean, ForeignKey, Integer, String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column
from app.helper.model import Base, id_key


class MenuType(str, Enum):
    MENU = 'menu'
    BUTTON = 'button'
    API = 'api'


class Department(Base):
    __tablename__ = 'sys_departments'
    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    parent_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('sys_departments.id', ondelete='CASECADE'))
    level: Mapped[int] = mapped_column(Integer, default=0)
    is_active: Mapped[str] = mapped_column(Boolean, default=True)


class Menu(Base):
    __tablename__ = 'sys_menu'
    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    type: Mapped[SqlEnum] = mapped_column(SqlEnum(MenuType), default=MenuType.MENU)
    icon: Mapped[str] = mapped_column(String(50), default='')
    component: Mapped[str] = mapped_column(String(100), default='')
    parent_id: Mapped[int] = mapped_column(ForeignKey('sys_menu.id', ondelete='CASECADE'))
    order: Mapped[Integer] = mapped_column(Integer, default=0)


class Permission(Base):
    __tablename__ = 'sys_permissions'


class Role(Base):
    __tablename__ = 'sys_roles'


class User(Base):
    __tablename__ = 'sys_user'
    id: Mapped[id_key] = mapped_column(init=False)
    username: Mapped[str] = mapped_column(String(32), init=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    nickname: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    def __str__(self) -> str:
        return f'id : {id} - {self.username}'

    def __repr__(self) -> str:
        return f'<User : id: {id} : {self.username}>'
