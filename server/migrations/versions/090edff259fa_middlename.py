"""middlename

Revision ID: 090edff259fa
Revises: 66d91d0c7df4
Create Date: 2021-09-19 18:12:20.561117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '090edff259fa'
down_revision = '66d91d0c7df4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cd_users', sa.Column('c_middlename', sa.String(length=500), nullable=True, comment='отчество'), schema='auth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cd_users', 'c_middlename', schema='auth')
    # ### end Alembic commands ###
