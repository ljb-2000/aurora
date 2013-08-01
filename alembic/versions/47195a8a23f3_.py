"""empty message

Revision ID: 47195a8a23f3
Revises: 141ceff13f17
Create Date: 2013-08-01 22:42:39.423301

"""

# revision identifiers, used by Alembic.
revision = '47195a8a23f3'
down_revision = '141ceff13f17'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    ### end Alembic commands ###
