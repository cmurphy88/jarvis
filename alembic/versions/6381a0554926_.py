"""empty message

Revision ID: 6381a0554926
Revises: c98722208c75
Create Date: 2022-07-06 11:23:04.906244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6381a0554926'
down_revision = 'c98722208c75'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('routine',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.TIME(), nullable=True),
    sa.Column('end_time', sa.TIME(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('routine')
    # ### end Alembic commands ###
