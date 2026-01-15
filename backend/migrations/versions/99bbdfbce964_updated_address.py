"""updated address

Revision ID: 99bbdfbce964
Revises: d2f6f4568523
Create Date: 2026-01-15 15:08:49.965404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99bbdfbce964'
down_revision = 'd2f6f4568523'
branch_labels = None
depends_on = None

geocode_enum = sa.Enum(
    'pending', 'success', 'failed',
    name='geocode_status'
)


def upgrade():
    geocode_enum.create(op.get_bind(), checkfirst=True)
    with op.batch_alter_table('addresses', schema=None) as batch_op:
        batch_op.add_column(sa.Column(
            'geocode_status', geocode_enum, nullable=False, server_default='pending'))


def downgrade():
    with op.batch_alter_table('addresses', schema=None) as batch_op:
        batch_op.drop_column('geocode_status')
    geocode_enum.drop(op.get_bind(), checkfirst=True)
