"""vma_csv binary table

Revision ID: 195bde5c67bf
Revises: 2e975775197f
Create Date: 2021-01-27 15:30:44.172001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '195bde5c67bf'
down_revision = '2e975775197f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vma_csv', sa.Column('legacy_variable', sa.String(), nullable=True))
    op.add_column('vma_csv', sa.Column('original_filename', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vma_csv', 'original_filename')
    op.drop_column('vma_csv', 'legacy_variable')
    # ### end Alembic commands ###
