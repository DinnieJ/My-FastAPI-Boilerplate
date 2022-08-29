"""create task table

Revision ID: 6b73f09eac89
Revises: 
Create Date: 2022-08-29 16:23:43.665772

"""
from email.policy import default
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b73f09eac89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'tb_tasks',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement='ignore_fk'),
        sa.Column('name', sa.String(255), nullable=True),
        sa.Column('user_id', sa.BigInteger, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, default="CURRENT_TIMESTAMP"),
        sa.Column('updated_at', sa.TIMESTAMP, default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP"),
    )


def downgrade() -> None:
    pass
