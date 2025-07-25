"""Initial migration

Revision ID: 7cae0e64dd39
Revises: 
Create Date: 2025-07-23 08:25:02.537911

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7cae0e64dd39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audit_log',
    sa.Column('log_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('action', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('log_id')
    )
    op.create_table('client',
    sa.Column('client_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('company_name', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('client_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('developer',
    sa.Column('developer_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('developer_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('manager',
    sa.Column('manager_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('contact_no', sa.String(length=15), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('manager_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('task',
    sa.Column('task_id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.Enum('todo', 'in_progress', 'done', name='taskstatus'), nullable=False),
    sa.Column('type', sa.Enum('bug', 'feature', 'task', name='tasktype'), nullable=False),
    sa.Column('priority', sa.String(length=10), nullable=True),
    sa.Column('project_id', sa.UUID(), nullable=False),
    sa.Column('subproject_id', sa.UUID(), nullable=True),
    sa.Column('sprint_id', sa.UUID(), nullable=True),
    sa.Column('epic_id', sa.UUID(), nullable=True),
    sa.Column('assigned_to_id', sa.UUID(), nullable=True),
    sa.Column('parent_task_id', sa.UUID(), nullable=True),
    sa.Column('estimated_hours', sa.Float(), nullable=True),
    sa.Column('logged_hours', sa.Float(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.Column('labels', sa.JSON(), nullable=True),
    sa.Column('custom_fields', sa.JSON(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['assigned_to_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['epic_id'], ['epic.epic_id'], ),
    sa.ForeignKeyConstraint(['parent_task_id'], ['task.task_id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.project_id'], ),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprint.sprint_id'], ),
    sa.ForeignKeyConstraint(['subproject_id'], ['subproject.subproject_id'], ),
    sa.PrimaryKeyConstraint('task_id')
    )
    op.create_table('attachment',
    sa.Column('attachment_id', sa.UUID(), nullable=False),
    sa.Column('file_name', sa.String(length=100), nullable=False),
    sa.Column('file_path', sa.String(length=255), nullable=False),
    sa.Column('task_id', sa.UUID(), nullable=True),
    sa.Column('ticket_id', sa.UUID(), nullable=True),
    sa.Column('created_by_id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.task_id'], ),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.ticket_id'], ),
    sa.PrimaryKeyConstraint('attachment_id')
    )
    op.create_table('comment',
    sa.Column('comment_id', sa.UUID(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('type', sa.Enum('task', 'ticket', name='commenttype'), nullable=False),
    sa.Column('task_id', sa.UUID(), nullable=True),
    sa.Column('ticket_id', sa.UUID(), nullable=True),
    sa.Column('created_by_id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.task_id'], ),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.ticket_id'], ),
    sa.PrimaryKeyConstraint('comment_id')
    )
    op.create_table('report',
    sa.Column('report_id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('task_id', sa.UUID(), nullable=True),
    sa.Column('project_id', sa.UUID(), nullable=True),
    sa.Column('manager_id', sa.UUID(), nullable=True),
    sa.Column('client_id', sa.UUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.client_id'], ),
    sa.ForeignKeyConstraint(['manager_id'], ['manager.manager_id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.project_id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.task_id'], ),
    sa.PrimaryKeyConstraint('report_id')
    )
    op.create_table('task_dependency',
    sa.Column('dependency_id', sa.UUID(), nullable=False),
    sa.Column('task_id', sa.UUID(), nullable=False),
    sa.Column('depends_on_task_id', sa.UUID(), nullable=False),
    sa.Column('dependency_type', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['depends_on_task_id'], ['task.task_id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.task_id'], ),
    sa.PrimaryKeyConstraint('dependency_id')
    )
    op.create_table('work_log',
    sa.Column('log_id', sa.UUID(), nullable=False),
    sa.Column('task_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('hours_logged', sa.Float(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('log_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['task.task_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('log_id')
    )
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('idx_board_project_id'))

    op.drop_table('board')
    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('idx_notification_status'))
        batch_op.drop_index(batch_op.f('idx_notification_user_id'))

    op.drop_table('notification')
    with op.batch_alter_table('story', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('idx_story_assigned_to_id'))
        batch_op.drop_index(batch_op.f('idx_story_epic_id'))
        batch_op.drop_index(batch_op.f('idx_story_priority'))
        batch_op.drop_index(batch_op.f('idx_story_project_id'))
        batch_op.drop_index(batch_op.f('idx_story_sprint_id'))
        batch_op.drop_index(batch_op.f('idx_story_status'))

    op.drop_table('story')
    with op.batch_alter_table('user_roles', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('idx_user_roles_primary'), postgresql_where='(is_primary = true)')
        batch_op.drop_index(batch_op.f('idx_user_roles_role_id'))
        batch_op.drop_index(batch_op.f('idx_user_roles_unique_primary'), postgresql_where='(is_primary = true)')
        batch_op.drop_index(batch_op.f('idx_user_roles_user_id'))

    op.drop_table('user_roles')
    with op.batch_alter_table('epic', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=postgresql.ENUM('open', 'in_progress', 'completed', 'cancelled', name='epic_status'),
               type_=sa.String(length=50),
               existing_nullable=True,
               existing_server_default=sa.text("'open'::epic_status"))
        batch_op.drop_index(batch_op.f('idx_epic_created_by_id'))
        batch_op.drop_index(batch_op.f('idx_epic_project_id'))
        batch_op.drop_index(batch_op.f('idx_epic_status'))

    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.alter_column('priority',
               existing_type=postgresql.ENUM('low', 'medium', 'high', 'critical', name='goal_priority'),
               type_=sa.Enum('LOW', 'MEDIUM', 'HIGH', 'URGENT', name='goalpriority'),
               existing_nullable=False,
               existing_server_default=sa.text("'medium'::goal_priority"))
        batch_op.alter_column('status',
               existing_type=postgresql.ENUM('pending', 'in_progress', 'completed', 'cancelled', name='goal_status'),
               type_=sa.Enum('PENDING', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED', name='goalstatus'),
               existing_nullable=False,
               existing_server_default=sa.text("'pending'::goal_status"))
        batch_op.alter_column('category',
               existing_type=postgresql.ENUM('personal', 'team', 'project', 'organizational', name='goal_category'),
               type_=sa.Enum('PERSONAL', 'TEAM', 'PROJECT', 'ORGANIZATIONAL', name='goalcategory'),
               existing_nullable=False,
               existing_server_default=sa.text("'personal'::goal_category"))
        batch_op.drop_index(batch_op.f('idx_goal_priority'))
        batch_op.drop_index(batch_op.f('idx_goal_project_id'))
        batch_op.drop_index(batch_op.f('idx_goal_status'))
        batch_op.drop_index(batch_op.f('idx_goal_target_date'))
        batch_op.drop_index(batch_op.f('idx_goal_user_id'))

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.alter_column('role_name',
               existing_type=postgresql.ENUM('admin', 'manager', 'developer', 'client', 'viewer', 'pending', name='role_name'),
               type_=sa.Enum('admin', 'manager', 'developer', 'client', 'viewer', 'pending', name='rolename'),
               existing_nullable=False)

    with op.batch_alter_table('sprint', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)
        batch_op.alter_column('end_date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)
        batch_op.drop_index(batch_op.f('idx_sprint_project_id'))
        batch_op.drop_index(batch_op.f('idx_sprint_subproject_id'))

    with op.batch_alter_table('ticket', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=postgresql.ENUM('open', 'in_progress', 'resolved', 'closed', name='ticket_status'),
               type_=sa.Enum('open', 'in_progress', 'closed', name='ticketstatus'),
               existing_nullable=False,
               existing_server_default=sa.text("'open'::ticket_status"))
        batch_op.alter_column('priority',
               existing_type=postgresql.ENUM('low', 'medium', 'high', name='ticket_priority'),
               type_=sa.Enum('low', 'medium', 'high', name='ticketpriority'),
               existing_nullable=False,
               existing_server_default=sa.text("'medium'::ticket_priority"))
        batch_op.drop_index(batch_op.f('idx_ticket_raised_by_id'))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))
        batch_op.drop_index(batch_op.f('idx_user_role_id'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('idx_user_role_id'), ['role_id'], unique=False)
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('ticket', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('idx_ticket_raised_by_id'), ['raised_by_id'], unique=False)
        batch_op.alter_column('priority',
               existing_type=sa.Enum('low', 'medium', 'high', name='ticketpriority'),
               type_=postgresql.ENUM('low', 'medium', 'high', name='ticket_priority'),
               existing_nullable=False,
               existing_server_default=sa.text("'medium'::ticket_priority"))
        batch_op.alter_column('status',
               existing_type=sa.Enum('open', 'in_progress', 'closed', name='ticketstatus'),
               type_=postgresql.ENUM('open', 'in_progress', 'resolved', 'closed', name='ticket_status'),
               existing_nullable=False,
               existing_server_default=sa.text("'open'::ticket_status"))

    with op.batch_alter_table('sprint', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('idx_sprint_subproject_id'), ['subproject_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_sprint_project_id'), ['project_id'], unique=False)
        batch_op.alter_column('end_date',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)
        batch_op.alter_column('start_date',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.alter_column('role_name',
               existing_type=sa.Enum('admin', 'manager', 'developer', 'client', 'viewer', 'pending', name='rolename'),
               type_=postgresql.ENUM('admin', 'manager', 'developer', 'client', 'viewer', 'pending', name='role_name'),
               existing_nullable=False)

    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('idx_goal_user_id'), ['user_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_goal_target_date'), ['target_date'], unique=False)
        batch_op.create_index(batch_op.f('idx_goal_status'), ['status'], unique=False)
        batch_op.create_index(batch_op.f('idx_goal_project_id'), ['project_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_goal_priority'), ['priority'], unique=False)
        batch_op.alter_column('category',
               existing_type=sa.Enum('PERSONAL', 'TEAM', 'PROJECT', 'ORGANIZATIONAL', name='goalcategory'),
               type_=postgresql.ENUM('personal', 'team', 'project', 'organizational', name='goal_category'),
               existing_nullable=False,
               existing_server_default=sa.text("'personal'::goal_category"))
        batch_op.alter_column('status',
               existing_type=sa.Enum('PENDING', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED', name='goalstatus'),
               type_=postgresql.ENUM('pending', 'in_progress', 'completed', 'cancelled', name='goal_status'),
               existing_nullable=False,
               existing_server_default=sa.text("'pending'::goal_status"))
        batch_op.alter_column('priority',
               existing_type=sa.Enum('LOW', 'MEDIUM', 'HIGH', 'URGENT', name='goalpriority'),
               type_=postgresql.ENUM('low', 'medium', 'high', 'critical', name='goal_priority'),
               existing_nullable=False,
               existing_server_default=sa.text("'medium'::goal_priority"))

    with op.batch_alter_table('epic', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('idx_epic_status'), ['status'], unique=False)
        batch_op.create_index(batch_op.f('idx_epic_project_id'), ['project_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_epic_created_by_id'), ['created_by_id'], unique=False)
        batch_op.alter_column('status',
               existing_type=sa.String(length=50),
               type_=postgresql.ENUM('open', 'in_progress', 'completed', 'cancelled', name='epic_status'),
               existing_nullable=True,
               existing_server_default=sa.text("'open'::epic_status"))

    op.create_table('user_roles',
    sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('role_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('assigned_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('assigned_by_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('is_primary', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['assigned_by_id'], ['user.user_id'], name=op.f('user_roles_assigned_by_id_fkey')),
    sa.ForeignKeyConstraint(['role_id'], ['role.role_id'], name=op.f('user_roles_role_id_fkey'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name=op.f('user_roles_user_id_fkey'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'role_id', name=op.f('user_roles_pkey'))
    )
    with op.batch_alter_table('user_roles', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('idx_user_roles_user_id'), ['user_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_user_roles_unique_primary'), ['user_id'], unique=True, postgresql_where='(is_primary = true)')
        batch_op.create_index(batch_op.f('idx_user_roles_role_id'), ['role_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_user_roles_primary'), ['user_id', 'is_primary'], unique=False, postgresql_where='(is_primary = true)')

    op.create_table('story',
    sa.Column('story_id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('acceptance_criteria', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('epic_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('project_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('sprint_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('todo', 'in_progress', 'done', 'blocked', name='story_status'), server_default=sa.text("'todo'::story_status"), autoincrement=False, nullable=True),
    sa.Column('priority', postgresql.ENUM('low', 'medium', 'high', 'critical', name='story_priority'), server_default=sa.text("'medium'::story_priority"), autoincrement=False, nullable=True),
    sa.Column('story_points', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('assigned_to_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('created_by_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('estimated_hours', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('actual_hours', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('start_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('due_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['assigned_to_id'], ['user.user_id'], name=op.f('story_assigned_to_id_fkey')),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.user_id'], name=op.f('story_created_by_id_fkey')),
    sa.ForeignKeyConstraint(['epic_id'], ['epic.epic_id'], name=op.f('story_epic_id_fkey')),
    sa.ForeignKeyConstraint(['project_id'], ['project.project_id'], name=op.f('story_project_id_fkey')),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprint.sprint_id'], name=op.f('story_sprint_id_fkey')),
    sa.PrimaryKeyConstraint('story_id', name=op.f('story_pkey'))
    )
    with op.batch_alter_table('story', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('idx_story_status'), ['status'], unique=False)
        batch_op.create_index(batch_op.f('idx_story_sprint_id'), ['sprint_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_story_project_id'), ['project_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_story_priority'), ['priority'], unique=False)
        batch_op.create_index(batch_op.f('idx_story_epic_id'), ['epic_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_story_assigned_to_id'), ['assigned_to_id'], unique=False)

    op.create_table('notification',
    sa.Column('notification_id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('status', postgresql.ENUM('unread', 'read', name='notification_status'), server_default=sa.text("'unread'::notification_status"), autoincrement=False, nullable=True),
    sa.Column('related_entity_type', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('related_entity_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('read_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name=op.f('notification_user_id_fkey')),
    sa.PrimaryKeyConstraint('notification_id', name=op.f('notification_pkey'))
    )
    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('idx_notification_user_id'), ['user_id'], unique=False)
        batch_op.create_index(batch_op.f('idx_notification_status'), ['status'], unique=False)

    op.create_table('board',
    sa.Column('board_id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('project_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['project.project_id'], name=op.f('board_project_id_fkey')),
    sa.PrimaryKeyConstraint('board_id', name=op.f('board_pkey'))
    )
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('idx_board_project_id'), ['project_id'], unique=False)

    op.drop_table('work_log')
    op.drop_table('task_dependency')
    op.drop_table('report')
    op.drop_table('comment')
    op.drop_table('attachment')
    op.drop_table('task')
    op.drop_table('manager')
    op.drop_table('developer')
    op.drop_table('client')
    op.drop_table('audit_log')
    # ### end Alembic commands ###
