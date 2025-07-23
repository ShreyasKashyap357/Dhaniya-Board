# Import all models to ensure they're registered with SQLAlchemy
from .models_models import db
from .role_models import Role
from .user_models import User
from .login_models import Login
from .team_models import Team
from .project_models import Project
from .subproject_models import Subproject
from .sprint_models import Sprint
from .epic_models import Epic
from .developer_team_models import DeveloperTeam
from .developer_project_models import DeveloperProject
from .manager_project_models import ManagerProject
from .client_models import Client
from .report_models import Report
from .goal_models import Goal
from .attachment_models import Attachment
from .audit_log_models import AuditLog
from .comment_models import Comment
from .notification_template_models import NotificationTemplate

# Add other model imports as needed
try:
    from .task_models import Task
except ImportError:
    pass

try:
    from .ticket_models import Ticket
except ImportError:
    pass

# Export commonly used models
__all__ = [
    'db', 'Role', 'User', 'Login', 'Team', 'Project', 'Subproject', 'Sprint', 'Epic',
    'DeveloperTeam', 'DeveloperProject', 'ManagerProject', 'Client', 'Report', 'Goal',
    'Attachment', 'AuditLog', 'Comment', 'NotificationTemplate'
]
