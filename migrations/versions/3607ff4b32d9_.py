"""empty message

Revision ID: 3607ff4b32d9
Revises: c7ace05f546c
Create Date: 2017-08-16 15:21:13.663270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3607ff4b32d9'
down_revision = 'c7ace05f546c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('betfreds', sa.Column('cliytd', sa.Integer(), nullable=True))
    op.add_column('betfreds', sa.Column('commiytd', sa.Float(), nullable=True))
    op.add_column('betfreds', sa.Column('impreytd', sa.Integer(), nullable=True))
    op.add_column('betfreds', sa.Column('ndytd', sa.Integer(), nullable=True))
    op.add_column('betfreds', sa.Column('regytd', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('betfreds', 'regytd')
    op.drop_column('betfreds', 'ndytd')
    op.drop_column('betfreds', 'impreytd')
    op.drop_column('betfreds', 'commiytd')
    op.drop_column('betfreds', 'cliytd')
    # ### end Alembic commands ###