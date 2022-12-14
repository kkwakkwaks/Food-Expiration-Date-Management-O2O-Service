"""empty message

Revision ID: 6e7f47b3af47
Revises: 4dde4414dc88
Create Date: 2022-09-08 06:49:52.136204

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6e7f47b3af47'
down_revision = '4dde4414dc88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('fridge', 'new_exp_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('fridge', 'create_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('user', 'gender',
               existing_type=sa.VARCHAR(length=100),
               nullable=False,
               existing_server_default=sa.text("'F'::character varying"))
    op.alter_column('user', 'region',
               existing_type=sa.VARCHAR(length=200),
               nullable=False,
               existing_server_default=sa.text("'서울'::character varying"))
    op.alter_column('user', 'age',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('30'))
    op.alter_column('user', 'create_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text("'2022-09-15 19:27:35.508'::timestamp without time zone"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'create_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text("'2022-09-15 19:27:35.508'::timestamp without time zone"))
    op.alter_column('user', 'age',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('30'))
    op.alter_column('user', 'region',
               existing_type=sa.VARCHAR(length=200),
               nullable=True,
               existing_server_default=sa.text("'서울'::character varying"))
    op.alter_column('user', 'gender',
               existing_type=sa.VARCHAR(length=100),
               nullable=True,
               existing_server_default=sa.text("'F'::character varying"))
    op.alter_column('fridge', 'create_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('fridge', 'new_exp_date',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###
