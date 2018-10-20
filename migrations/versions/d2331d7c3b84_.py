"""empty message

Revision ID: d2331d7c3b84
Revises: 0ee5a8f99d4f
Create Date: 2018-10-20 17:20:50.999546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2331d7c3b84'
down_revision = '0ee5a8f99d4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_rated_episodes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.Column('liked', sa.Boolean(), nullable=True),
    sa.Column('disliked', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['episode_id'], ['episode.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'episode_id')
    )
    op.drop_table('user_liked_episodes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_liked_episodes',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('episode_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['episode_id'], ['episode.id'], name='user_liked_episodes_episode_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='user_liked_episodes_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', 'episode_id', name='user_liked_episodes_pkey')
    )
    op.drop_table('user_rated_episodes')
    # ### end Alembic commands ###
