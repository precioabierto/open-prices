"""add product.price_per field

Revision ID: a8ad2f078f3f
Revises: 007443669adc
Create Date: 2024-01-11 09:14:25.778905

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a8ad2f078f3f"
down_revision: Union[str, None] = "007443669adc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "prices",
        sa.Column(
            "price_per",
            sa.String(length=255),
            nullable=True,
        ),
    )
    op.execute(
        "UPDATE prices SET price_per = 'KILOGRAM' WHERE price_per IS NULL AND category_tag IS NOT NULL;"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("prices", "price_per")
    # ### end Alembic commands ###