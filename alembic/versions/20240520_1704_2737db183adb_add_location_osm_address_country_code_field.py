"""Add Location osm_address_country_code field

Revision ID: 2737db183adb
Revises: dd4776351212
Create Date: 2024-05-20 17:04:40.347002

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2737db183adb"
down_revision: Union[str, None] = "dd4776351212"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "locations", sa.Column("osm_address_country_code", sa.String(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("locations", "osm_address_country_code")
    # ### end Alembic commands ###
