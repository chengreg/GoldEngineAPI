"""fix enum bugs

Revision ID: 393655b2eb15
Revises: f3b053300fbe
Create Date: 2023-09-20 23:37:37.968027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '393655b2eb15'
down_revision: Union[str, None] = 'f3b053300fbe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('social_account', 'provider',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Enum('GOOGLE', 'FACEBOOK', 'TWITTER', 'GITHUB', 'LINKEDIN', 'WEIBO', 'WEIXIN', 'QQ', 'ALIPAY', name='providerenum'),
               existing_comment='第三方平台',
               existing_nullable=False)
    op.add_column('user_profile', sa.Column('sex', sa.Enum('MALE', 'FEMALE', 'OTHER', name='sexenum'), nullable=True, comment='性别'))
    op.drop_column('user_profile', 'gender')
    op.alter_column('users', 'status',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.Enum('ACTIVE', 'INACTIVE', 'DELETED', 'BLOCKED', 'LOCKED', 'PENDING', name='usersstatusenum'),
               existing_comment='用户状态',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'status',
               existing_type=sa.Enum('ACTIVE', 'INACTIVE', 'DELETED', 'BLOCKED', 'LOCKED', 'PENDING', name='usersstatusenum'),
               type_=mysql.VARCHAR(length=10),
               existing_comment='用户状态',
               existing_nullable=False)
    op.add_column('user_profile', sa.Column('gender', mysql.VARCHAR(length=2), nullable=True, comment='性别'))
    op.drop_column('user_profile', 'sex')
    op.alter_column('social_account', 'provider',
               existing_type=sa.Enum('GOOGLE', 'FACEBOOK', 'TWITTER', 'GITHUB', 'LINKEDIN', 'WEIBO', 'WEIXIN', 'QQ', 'ALIPAY', name='providerenum'),
               type_=mysql.VARCHAR(length=50),
               existing_comment='第三方平台',
               existing_nullable=False)
    # ### end Alembic commands ###
