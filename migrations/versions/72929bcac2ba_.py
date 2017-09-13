"""empty message

Revision ID: 72929bcac2ba
Revises: 73c26fef253b
Create Date: 2017-09-13 13:15:08.626000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72929bcac2ba'
down_revision = '73c26fef253b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('logs', sa.Column('managed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('logs', 'managed')
    # ### end Alembic commands ###
