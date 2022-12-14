"""empty message

Revision ID: 88272eb907b1
Revises: 5ba7d6a714e2
Create Date: 2022-09-08 08:33:53.671265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88272eb907b1'
down_revision = '5ba7d6a714e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('fridge', 'product_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True,
               existing_server_default=sa.text('1'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('fridge', 'product_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True,
               existing_server_default=sa.text('1'))
    # ### end Alembic commands ###
