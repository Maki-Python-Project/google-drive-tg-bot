"""test migration

Revision ID: 02b9958d0d18
Revises: 
Create Date: 2022-11-28 13:43:12.920048

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '02b9958d0d18'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userinfo',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userinfo')
    # ### end Alembic commands ###