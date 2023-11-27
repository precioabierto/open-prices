"""Add Proof.type field

Revision ID: cce1da5c6733
Revises: 012466c0013e
Create Date: 2023-11-25 17:26:49.022693

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "cce1da5c6733"
down_revision: Union[str, None] = "012466c0013e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("proofs", sa.Column("type", sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("proofs", "type")
    # ### end Alembic commands ###
