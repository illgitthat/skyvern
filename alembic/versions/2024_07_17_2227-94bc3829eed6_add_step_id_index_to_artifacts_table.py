"""add step_id index to artifacts table

Revision ID: 94bc3829eed6
Revises: 370cb81c73e7
Create Date: 2024-07-17 22:27:30.734057+00:00

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "94bc3829eed6"
down_revision: Union[str, None] = "370cb81c73e7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_artifacts_step_id"), "artifacts", ["step_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_artifacts_step_id"), table_name="artifacts")
    # ### end Alembic commands ###