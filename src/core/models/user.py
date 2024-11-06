from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    foo: Mapped[str]
    bar: Mapped[str]

    __table_args__ = (UniqueConstraint("foo", "bar"),)
