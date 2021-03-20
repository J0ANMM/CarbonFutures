"""workbook commit id

Revision ID: 87aa6970939f
Revises: 2524d9bf1bbc
Create Date: 2020-12-22 16:56:37.127581

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '87aa6970939f'
down_revision = '2524d9bf1bbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('workbook', sa.Column('commit', postgresql.UUID(as_uuid=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workbook', 'commit')
    # ### end Alembic commands ###