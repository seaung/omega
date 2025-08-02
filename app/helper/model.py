from datetime import datetime, timezone
from typing import Annotated

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, declared_attr, mapped_column


id_key = Annotated[
    int,
    mapped_column(
        BigInteger,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=True,
        sort_order=-999,
        comment='ID主键',
    )
]


class UserMixin(MappedAsDataclass):
    created_by: Mapped[int] = mapped_column(sort_order=998, comment='创建者')
    updated_by: Mapped[int | None] = mapped_column(init=False, default=None, sort_order=998, comment='修改者')



class DateTimeMixin(MappedAsDataclass):
    created_time: Mapped[datetime] =  mapped_column(
        DateTime(timezone=True),
        init=False,
        sort_order=999,
        comment='创建时间',
    )
    updated_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        init=False,
        sort_order=999,
        comment='更新时间',
    )


class MappedBase(AsyncAttrs, DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    @declared_attr.directive
    def __table_args__(cls) -> dict:
        return {'commnet': cls.__doc__ or ''}


class DataClassBase(MappedAsDataclass, MappedBase):
    __abstract__ = True


class Base(DataClassBase, DateTimeMixin):
    __abstract__ = True
