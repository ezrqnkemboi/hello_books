"""empty message

Revision ID: ca8125d7b641
Revises: eafd17502a68
Create Date: 2018-04-10 19:17:10.374058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca8125d7b641'
down_revision = 'eafd17502a68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('histories', sa.Column('return_status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('histories', 'return_status')
    # ### end Alembic commands ###
