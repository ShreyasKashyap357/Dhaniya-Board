# 🌿 Dhaniya - Natural Project Management System

[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive project management system built with Flask and PostgreSQL, featuring Jira-like kanban boards, role-based access control, and real-time analytics. "Dhaniya" (Hindi for Coriander) represents the natural, organic approach to project management.

## ✨ Features

### 🎯 Core Functionality
- **Kanban Boards** - Drag-and-drop task management with customizable columns
- **Project Management** - Create, track, and manage projects with goals and deadlines
- **Sprint Management** - Agile sprint planning and tracking
- **Task Tracking** - Comprehensive task management with priorities and assignments
- **Team Collaboration** - Team member management and role assignments

### 🔐 Authentication & Authorization
- **Role-Based Access Control** - Admin, Manager, Developer, and Viewer roles
- **User Management** - Complete user lifecycle management
- **Secure Authentication** - Flask-Login integration with session management

### 📊 Analytics & Reporting
- **Admin Dashboard** - Real-time system statistics and user analytics
- **Project Analytics** - Task completion rates, team performance metrics
- **System Health Monitoring** - Database, API, and storage monitoring
- **User Activity Tracking** - Recent actions and system events

### 🎨 User Experience
- **Responsive Design** - Bootstrap-powered mobile-friendly interface
- **Natural Theme** - Organic color scheme with "Dhaniya" green branding
- **Interactive UI** - Modern components with smooth animations
- **Flash Messaging** - Real-time user feedback system

## 🛠️ Technology Stack

**Backend:**
- **Flask 2.3.3** - Web framework
- **SQLAlchemy 2.0.41** - ORM and database management
- **PostgreSQL** - Primary database
- **Flask-Login 0.6.2** - User session management
- **Flask-WTF 1.2.1** - Form handling and validation

**Frontend:**
- **Bootstrap 5** - Responsive CSS framework
- **Jinja2 3.1.6** - Template engine
- **Font Awesome** - Icons and UI elements
- **Custom CSS** - Natural theme styling

**Development:**
- **Python 3.8+** - Programming language
- **psycopg2-binary 2.9.10** - PostgreSQL adapter

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dhaniya-project-management.git
   cd dhaniya-project-management
   ```

2. **Create virtual environment**
   ```bash
   python -m venv flask-env
   # Windows
   flask-env\Scripts\activate
   # macOS/Linux
   source flask-env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   # Create PostgreSQL database
   createdb dhaniya_db
   
   # Initialize database with schema
   python -c "from app import db; db.create_all()"
   
   # Load sample data (optional)
   psql dhaniya_db < sample_data.sql
   ```

5. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=postgresql://username:password@localhost/dhaniya_db
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` in your browser.

## 📁 Project Structure

```
dhaniya-project-management/
├── app.py                      # Main application entry point
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── credentials.txt             # Sample credentials
├── jira_board_schema.sql      # Database schema
├── sample_data.sql            # Sample data for testing
├── controllers/               # Business logic controllers
│   ├── auth_controllers.py
│   ├── dashboard_controllers.py
│   ├── project_controllers.py
│   ├── task_controllers.py
│   └── ...
├── models/                    # Database models
│   ├── __init__.py
│   ├── user_models.py
│   ├── project_models.py
│   ├── task_models.py
│   └── ...
├── routes/                    # URL routing
│   ├── auth_routes.py
│   ├── admin_routes.py
│   └── ...
├── forms/                     # WTForms form definitions
│   ├── auth_forms.py
│   ├── project_forms.py
│   └── ...
├── templates/                 # Jinja2 HTML templates
│   ├── base.html
│   ├── dashboard_admin.html
│   ├── project_detail.html
│   └── ...
└── static/                    # Static assets
    ├── css/
    ├── js/
    └── images/
```

## 👥 User Roles & Permissions

| Role | Permissions |
|------|-------------|
| **Admin** | Full system access, user management, system settings, all projects |
| **Manager** | Project creation/management, team assignment, reporting |
| **Developer** | Task management, project participation, status updates |
| **Viewer** | Read-only access to assigned projects and tasks |

## 🔧 Configuration

### Database Configuration
Update `config.py` with your database settings:
```python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dhaniya_db'
```

### Feature Flags
Enable/disable features in `config.py`:
```python
ENABLE_REGISTRATION = True
REQUIRE_EMAIL_VERIFICATION = False
MAX_PROJECTS_PER_USER = 10
```

## 📊 Admin Dashboard Features

- **Real-time Statistics** - User counts, project status, task metrics
- **System Health Monitoring** - Database, API, and storage status
- **User Management** - Create, edit, deactivate users
- **Role Distribution** - Visual breakdown of user roles
- **Activity Tracking** - Recent system events and user actions
- **Quick Actions** - One-click access to common admin tasks

## 🎨 Theming

The application uses a natural "Dhaniya" green theme:
- Primary Color: `#28a745` (Bootstrap Success)
- Secondary Color: `#20c997` (Bootstrap Teal)
- Accent Colors: Natural earth tones
- Typography: Clean, readable fonts with good contrast

## 🧪 Sample Data

The project includes sample data with:
- 5 sample users across different roles
- 3 demo projects (Project Lehsun, Project Haldi, Project Mirch)
- Sample tasks, sprints, and team assignments
- Realistic project timelines and goals

Load sample data:
```bash
psql your_database < sample_data.sql
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by natural project management philosophies
- Built with love using Flask and PostgreSQL
- Bootstrap for responsive design
- Font Awesome for beautiful icons
- The open-source community for amazing tools

## 📞 Support

For support, email shreyas.venur@gmail.com or create an issue in this repository.

---

Made with 🌿 by [Shreyas Kashyap, Jaideep Yadav, Ayush Kumar Karmi, Suprim Raja] | PEP (Personal Enhancement Program) Python Full Stack Major Project