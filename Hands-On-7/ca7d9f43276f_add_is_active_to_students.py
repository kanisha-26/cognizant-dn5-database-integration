"""add is_active to students

Revision ID: ca7d9f43276f
Revises: 0d4ca677e09c
Create Date: 2026-06-14

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "ca7d9f43276f"
down_revision: Union[str, Sequence[str], None] = "0d4ca677e09c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "students",
        sa.Column("is_active", sa.Boolean(), nullable=True)
    )


def downgrade() -> None:
    op.drop_column("students", "is_active")
