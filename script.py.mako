<%text>
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
</%text>

from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
