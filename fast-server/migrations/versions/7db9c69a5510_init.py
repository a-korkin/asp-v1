"""init

Revision ID: 7db9c69a5510
Revises: 
Create Date: 2021-09-25 19:24:54.859946

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7db9c69a5510'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cd_entities',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False, comment='идентификатор'),
    sa.PrimaryKeyConstraint('id'),
    schema='common',
    comment='сущности'
    )
    op.create_table('cd_users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('username', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['common.cd_entities.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username'),
    schema='auth',
    comment='пользователи'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cd_users', schema='auth')
    op.drop_table('cd_entities', schema='common')
    # ### end Alembic commands ###