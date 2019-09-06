"""empty message

Revision ID: 317a899a09f1
Revises: 7e9fbb7c2575
Create Date: 2019-09-02 05:59:41.276272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '317a899a09f1'
down_revision = '7e9fbb7c2575'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organisation', 'namespace')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organisation', sa.Column('namespace', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
