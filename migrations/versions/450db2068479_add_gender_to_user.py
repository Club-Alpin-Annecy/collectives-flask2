"""Add gender to user

Revision ID: 450db2068479
Revises: c7fe6453ad90
Create Date: 2020-01-11 21:01:13.772899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '450db2068479'
down_revision = 'c7fe6453ad90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column(   'gender',
                                        sa.Integer(),
                                        nullable=False,
                                        server_default='0')
                )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'gender')
    # ### end Alembic commands ###
