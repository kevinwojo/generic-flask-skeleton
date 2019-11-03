"""create table for example model

Revision ID: 623d05ab72e5
Revises:
Create Date: 2019-11-03 10:57:07.654282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "623d05ab72e5"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "resource",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=True),
        sa.Column(
            "created", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("resource")
    # ### end Alembic commands ###