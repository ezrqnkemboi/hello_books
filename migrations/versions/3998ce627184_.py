"""empty message

Revision ID: 3998ce627184
Revises: 19add00ef7a1
Create Date: 2018-04-20 00:17:26.202952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3998ce627184'
down_revision = '19add00ef7a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('copies', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'copies')
    # ### end Alembic commands ###