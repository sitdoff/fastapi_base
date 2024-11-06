"""Init migrationi

Revision ID: ffca62791e82
Revises: 8b3975846f89
Create Date: 2024-11-06 20:09:49.279799

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ffca62791e82"
down_revision: Union[str, None] = "8b3975846f89"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("foo", sa.String(), nullable=False),
        sa.Column("bar", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("foo", "bar", name=op.f("uq_users_foo")),
        sa.UniqueConstraint("username", name=op.f("uq_users_username")),
    )


def downgrade() -> None:
    op.drop_table("users")
