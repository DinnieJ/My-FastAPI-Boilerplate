"""set username unique

Revision ID: 225d83e35ecd
Revises: 83ffc27bed28
Create Date: 2022-08-30 13:49:47.776206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '225d83e35ecd'
down_revision = '83ffc27bed28'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("uq_username", "tb_users", ["username"])
    op.alter_column(existing_type=sa.BigInteger,table_name="tb_users", column_name="id", autoincrement=True, existing_autoincrement=True, nullable=False)


def downgrade() -> None:
    op.drop_constraint("uq_username", "tb_users")
    # op.create_unique_constraint("uq_username", "tb_users", ["username"])
    op.alter_column(existing_type=sa.BigInteger, table_name="tb_users", column_name="id", autoincrement=False, existing_autoincrement=False, nullable=False)
