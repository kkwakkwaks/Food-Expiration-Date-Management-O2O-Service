"""empty message

Revision ID: aa37ed7bd6f7
Revises: 88272eb907b1
Create Date: 2022-09-08 10:26:07.675374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa37ed7bd6f7'
down_revision = '88272eb907b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('barcode',
    sa.Column('barcode_id', sa.Integer(), nullable=False),
    sa.Column('barcode', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('barcode_id', name=op.f('pk_barcode'))
    )
    op.create_table('barcode__categories',
    sa.Column('b_category_id', sa.Integer(), nullable=False),
    sa.Column('b_category_name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('b_category_id', name=op.f('pk_barcode__categories'))
    )
    op.add_column('fridge', sa.Column('remain_date', sa.DateTime(), server_default='2022-09-01', nullable=True, auto_now_add=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fridge', 'remain_date')
    op.drop_table('barcode__categories')
    op.drop_table('barcode')
    # ### end Alembic commands ###
