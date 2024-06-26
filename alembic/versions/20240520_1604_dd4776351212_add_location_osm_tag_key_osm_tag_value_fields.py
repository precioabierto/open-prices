"""Add Location osm_tag_key & osm_tag_value fields

Revision ID: dd4776351212
Revises: 3e6064e45f9a
Create Date: 2024-05-20 16:04:30.068721

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "dd4776351212"
down_revision: Union[str, None] = "3e6064e45f9a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("locations", sa.Column("osm_tag_key", sa.String(), nullable=True))
    op.add_column("locations", sa.Column("osm_tag_value", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("locations", "osm_tag_value")
    op.drop_column("locations", "osm_tag_key")
    # ### end Alembic commands ###
