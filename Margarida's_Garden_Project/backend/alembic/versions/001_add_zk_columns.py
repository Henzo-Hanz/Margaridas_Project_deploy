"""Add Zero Knowledge columns (encryption_salt, client_encrypted)

Revision ID: 001_zk
Revises:
Create Date: 2025-02-22

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "001_zk"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("encryption_salt", sa.Text(), nullable=True))
    op.add_column("credentials", sa.Column("client_encrypted", sa.Boolean(), nullable=False, server_default=sa.false()))


def downgrade() -> None:
    op.drop_column("credentials", "client_encrypted")
    op.drop_column("users", "encryption_salt")
