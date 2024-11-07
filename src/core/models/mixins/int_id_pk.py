from sqlalchemy.orm import Mapped, mapped_column


class IntIdPkMixin:
    """
    Миксин задает primary key для модели.
    """

    id: Mapped[int] = mapped_column(primary_key=True)
