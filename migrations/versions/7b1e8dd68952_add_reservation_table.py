"""add reservation table

Revision ID: 7b1e8dd68952
Revises: 0650626ecbf1
Create Date: 2022-12-22 16:53:15.943384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b1e8dd68952'
down_revision = '0650626ecbf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reserved_restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('businessId', sa.String(length=22), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('location', sa.String(length=80), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=False),
    sa.Column('yelp_url', sa.Text(), nullable=False),
    sa.Column('people', sa.Integer(), nullable=False),
    sa.Column('dt', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('businessId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reserved_restaurants')
    # ### end Alembic commands ###
