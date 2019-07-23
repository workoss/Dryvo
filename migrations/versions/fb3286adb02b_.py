"""empty message

Revision ID: fb3286adb02b
Revises: a016145093d8
Create Date: 2019-07-15 16:27:08.144798

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from server.api.database.models import AppointmentType

# revision identifiers, used by Alembic.
revision = "fb3286adb02b"
down_revision = "a016145093d8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "lessons",
        sa.Column(
            "type",
            sa.INTEGER(),
            nullable=False,
            server_default=str(AppointmentType.LESSON.value),
            default=AppointmentType.LESSON.value,
        ),
    )
    op.rename_table("lessons", "appointments")
    op.drop_table("tests")
    op.drop_constraint(
        "lesson_topics_lesson_id_fkey", "lesson_topics", type_="foreignkey"
    )
    op.create_foreign_key(
        "lesson_topics_lesson_id_fkey",
        "lesson_topics",
        "appointments",
        ["lesson_id"],
        ["id"],
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "lesson_topics_lesson_id_fkey", "lesson_topics", type_="foreignkey"
    )
    op.create_foreign_key(
        "lesson_topics_lesson_id_fkey",
        "lesson_topics",
        "lessons",
        ["lesson_id"],
        ["id"],
    )
    op.create_table(
        "tests",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("student_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("result", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("content", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("time", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["student_id"], ["students.id"], name="tests_student_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="tests_pkey"),
    )
    op.rename_table("appointments", "lessons")
    # ### end Alembic commands ###
