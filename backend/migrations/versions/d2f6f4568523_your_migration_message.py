"""Create initial app tables

Revision ID: d2f6f4568523
Revises: 04c44383601f
Create Date: 2025-12-09 23:42:36.660375
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd2f6f4568523'
down_revision = '04c44383601f'
branch_labels = None
depends_on = None


def upgrade():
    # Create job_categories table
    op.create_table(
        'job_categories',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
    )

    # Create skills table
    op.create_table(
        'skills',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
    )

    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(length=150),
                  nullable=False, unique=True),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    )

    # Create companies table
    op.create_table(
        'companies',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('address_id', sa.Integer(), sa.ForeignKey(
            'addresses.id'), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    )

    # Create user_skills table (many-to-many)
    op.create_table(
        'user_skills',
        sa.Column('user_id', sa.Integer(), sa.ForeignKey(
            'users.id'), primary_key=True),
        sa.Column('skill_id', sa.Integer(), sa.ForeignKey(
            'skills.id'), primary_key=True),
    )

    # Create job_posts table
    op.create_table(
        'job_posts',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('job_category_id', sa.Integer(), sa.ForeignKey(
            'job_categories.id'), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey(
            'companies.id'), nullable=False),
        sa.Column('salary', sa.Float(), nullable=False),
        sa.Column('salary_type', sa.String(length=20), nullable=True),
        sa.Column('address_id', sa.Integer(), sa.ForeignKey(
            'addresses.id'), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    )

    # Create job_post_skills table (many-to-many)
    op.create_table(
        'job_post_skills',
        sa.Column('job_post_id', sa.Integer(), sa.ForeignKey(
            'job_posts.id'), primary_key=True),
        sa.Column('skill_id', sa.Integer(), sa.ForeignKey(
            'skills.id'), primary_key=True),
        sa.Column('required', sa.Boolean(), nullable=False),
    )


def downgrade():
    # Drop all tables in reverse order
    op.drop_table('job_post_skills')
    op.drop_table('job_posts')
    op.drop_table('user_skills')
    op.drop_table('companies')
    op.drop_table('users')
    op.drop_table('skills')
    op.drop_table('job_categories')
