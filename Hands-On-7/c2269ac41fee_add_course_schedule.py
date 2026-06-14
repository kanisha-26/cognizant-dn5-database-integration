"""add course schedule

Revision ID: c2269ac41fee
Revises: ca7d9f43276f
Create Date: 2026-06-14

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "c2269ac41fee"
down_revision: Union[str, Sequence[str], None] = "ca7d9f43276f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "course_schedules",
        sa.Column("schedule_id", sa.Integer(), primary_key=True),
        sa.Column("course_id", sa.Integer(), sa.ForeignKey("courses.course_id")),
        sa.Column("day_of_week", sa.String(20)),
        sa.Column("start_time", sa.String(20)),
        sa.Column("end_time", sa.String(20))
    )


def downgrade() -> None:
    op.drop_table("course_schedules")
