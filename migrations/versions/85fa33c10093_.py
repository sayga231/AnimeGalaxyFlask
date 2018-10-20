"""empty message

Revision ID: 85fa33c10093
Revises: a8eb42c36ec7
Create Date: 2018-10-14 00:57:00.454325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85fa33c10093'
down_revision = 'a8eb42c36ec7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('episode_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'video', 'episode', ['episode_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'video', type_='foreignkey')
    op.drop_column('video', 'episode_id')
    # ### end Alembic commands ###
