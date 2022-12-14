"""empty message

Revision ID: 8104e925bab3
Revises: d62c7e50a7d0
Create Date: 2022-09-08 18:16:50.765949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8104e925bab3'
down_revision = 'd62c7e50a7d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('barcode__categories',
    sa.Column('b_category_id', sa.Integer(), nullable=False),
    sa.Column('b_category_name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('b_category_id', name=op.f('pk_barcode__categories'))
    )
    op.create_foreign_key(op.f('fk_answer_user_id_user'), 'answer', 'user', ['user_id'], ['id'])
    op.create_foreign_key(op.f('fk_answer_question_id_question'), 'answer', 'question', ['question_id'], ['id'])
    op.add_column('fridge', sa.Column('product_Id', sa.Integer(), nullable=False))
    op.alter_column('fridge', 'product',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('fridge', 'subclass',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.create_unique_constraint(op.f('uq_fridge_product'), 'fridge', ['product'])
    op.create_foreign_key(op.f('fk_fridge_user_id_user'), 'fridge', 'user', ['user_id'], ['id'])
    op.alter_column('question', 'subject',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.create_foreign_key(op.f('fk_question_user_id_user'), 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'gender',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('user', 'region',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.create_unique_constraint(op.f('uq_user_email'), 'user', ['email'])
    op.create_unique_constraint(op.f('uq_user_username'), 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_user_username'), 'user', type_='unique')
    op.drop_constraint(op.f('uq_user_email'), 'user', type_='unique')
    op.alter_column('user', 'region',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column('user', 'gender',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.drop_constraint(op.f('fk_question_user_id_user'), 'question', type_='foreignkey')
    op.alter_column('question', 'subject',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.drop_constraint(op.f('fk_fridge_user_id_user'), 'fridge', type_='foreignkey')
    op.drop_constraint(op.f('uq_fridge_product'), 'fridge', type_='unique')
    op.alter_column('fridge', 'subclass',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('fridge', 'product',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_column('fridge', 'product_Id')
    op.drop_constraint(op.f('fk_answer_question_id_question'), 'answer', type_='foreignkey')
    op.drop_constraint(op.f('fk_answer_user_id_user'), 'answer', type_='foreignkey')
    op.drop_table('barcode__categories')
    # ### end Alembic commands ###
