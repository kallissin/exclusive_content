"""Adding ContentModel

Revision ID: 6e55cb1c0a5c
Revises: 
Create Date: 2023-11-02 14:53:21.525483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from src.infra.db_models.content_db_models import CATEGORY


# revision identifiers, used by Alembic.
revision: str = '6e55cb1c0a5c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contents',
    sa.Column('content_id', sa.UUID(), nullable=False),
    sa.Column('category', sqlalchemy_utils.types.choice.ChoiceType(CATEGORY), nullable=False),
    sa.Column('title', sa.Unicode(length=128), nullable=False),
    sa.Column('content', sa.UnicodeText(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('content_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contents')
    # ### end Alembic commands ###
