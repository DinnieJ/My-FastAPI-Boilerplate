"""create users table

Revision ID: 83ffc27bed28
Revises: 6b73f09eac89
Create Date: 2022-08-30 09:40:18.520132

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '83ffc27bed28'
down_revision = '6b73f09eac89'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("tb_users",
        sa.Column('id', sa.BigInteger, autoincrement="ignore_fk"),
        sa.Column('username', sa.String(100), nullable=False),
        sa.Column('password', sa.String(64), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.TIMESTAMP, 
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), 
        )
    )

    op.create_primary_key("pk_users", "tb_users", ["id"])
    pass


def downgrade() -> None:
    op.drop_table("tb_users")
