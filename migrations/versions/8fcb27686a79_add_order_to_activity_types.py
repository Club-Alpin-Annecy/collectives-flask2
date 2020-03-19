"""Add order to activity types

Revision ID: 8fcb27686a79
Revises: e9f048fe1358
Create Date: 2020-03-14 13:35:06.972551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fcb27686a79'
down_revision = 'e9f048fe1358'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity_types', sa.Column('order', sa.Integer(), nullable=False, server_default="1"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activity_types', 'order')
    # ### end Alembic commands ###