"""empty message

Revision ID: 5727df02f8bf
Revises:
Create Date: 2018-02-14 10:26:57.121153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5727df02f8bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=80), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('access_token', sa.String(length=257), nullable=False),
                    sa.Column('request_token', sa.String(length=257), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    op.create_table('games',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('word', sa.String(length=32), nullable=False),
                    sa.Column('guesses', sa.ARRAY(sa.String(32)), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    op.drop_table('users')
    # ### end Alembic commands ###
