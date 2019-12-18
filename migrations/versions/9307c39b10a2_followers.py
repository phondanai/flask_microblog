"""followers

Revision ID: 9307c39b10a2
Revises: 27e19395fc6d
Create Date: 2019-12-17 17:01:42.264559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9307c39b10a2'
down_revision = '27e19395fc6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###