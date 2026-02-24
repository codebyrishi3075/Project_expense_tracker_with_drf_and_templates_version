# 💰 Expense Tracker & Budget Planner

A comprehensive web-based personal finance application built with **Django REST Framework (DRF)** and **Django Templates (MVT)**, designed to help users log expenses, set budgets, visualize spending patterns, and manage their finances effectively.

**Live Demo:** [Coming Soon]  
**API Documentation:** [Coming Soon]  
**Frontend:** [Coming Soon]

---

## 🎯 Project Overview

This project is structured as a full-stack application with dual implementation approaches:

1. **Django REST Framework (DRF) Version** - A robust API-based backend with separate React frontend
2. **Django Templates (MVT) Version** - A traditional server-side rendered approach

Both versions share the same core business logic and database structure, making this an excellent portfolio project demonstrating modern web development practices.

---

## ✨ Key Features

### 💰 Expense Management
- ✅ Log daily, weekly, and monthly expenses
- ✅ Add detailed expense information (amount, category, date, notes)
- ✅ Edit and delete expense entries
- ✅ Bulk import via CSV (coming soon)

### 📊 Budget Planning & Alerts
- ✅ Set monthly/weekly budgets per category
- ✅ Define spending limits
- ✅ Real-time budget vs. actual spending comparison
- ✅ Budget alert notifications (coming soon)

### 📈 Analytics & Visualization
- ✅ Interactive charts using Recharts (DRF + React version)
- ✅ Spending trends analysis
- ✅ Category-wise breakdown (Pie charts)
- ✅ Time-series spending visualization (Line charts)
- ✅ Period-over-period comparison

### 🔍 Advanced Filtering & Search
- ✅ Filter by date range
- ✅ Filter by category
- ✅ Filter by amount range
- ✅ Combined filter support

### 👤 User Management
- ✅ User registration & authentication (JWT for DRF)
- ✅ Secure password hashing
- ✅ User profile management
- ✅ Customizable settings (currency, timezone, budget limits)

### 🎨 User Experience
- ✅ Mobile-first responsive design
- ✅ Minimalist, clean dashboard
- ✅ Intuitive navigation
- ✅ Dark mode support (coming soon)

---

## 🏗️ Project Architecture

### Technology Stack

#### Backend
- **Framework:** Django 4.x + Django REST Framework
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Authentication:** JWT (DRF version) / Session-based (Template version)
- **Validation:** Django Forms & Serializers
- **API Documentation:** DRF Swagger/OpenAPI

#### Frontend (DRF Version)
- **Library:** React 18.x
- **State Management:** Redux / Context API
- **Charts:** Recharts
- **Styling:** Tailwind CSS / Bootstrap
- **HTTP Client:** Axios

#### Frontend (Template Version)
- **Templating:** Django Templates
- **Styling:** Bootstrap 5 / Tailwind CSS
- **JavaScript:** Vanilla JS / Alpine.js

### Directory Structure

```
expense_tracker_with_DRF_and_templates/
│
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment variables template
├── .gitignore                     # Git ignore rules
├── README.md                      # This file
│
├── config/                        # Project configuration
│   ├── __init__.py
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL routing
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
│
├── accounts/                      # User authentication app
│   ├── models.py                 # Custom User model
│   ├── serializers.py            # DRF serializers
│   ├── views.py                  # Authentication views
│   ├── urls.py                   # App-specific URLs
│   ├── tests.py                  # Unit tests
│   └── migrations/
│
├── expenses/                      # Expense management app
│   ├── models.py                 # Expense & Category models
│   ├── serializers.py            # DRF serializers
│   ├── views.py                  # API & template views
│   ├── urls.py                   # App-specific URLs
│   ├── tests.py                  # Unit tests
│   ├── forms.py                  # Django forms (Template version)
│   └── migrations/
│
├── budgets/                       # Budget management app
│   ├── models.py                 # Budget & BudgetLimit models
│   ├── serializers.py            # DRF serializers
│   ├── views.py                  # API & template views
│   ├── urls.py                   # App-specific URLs
│   ├── tests.py                  # Unit tests
│   ├── forms.py                  # Django forms (Template version)
│   └── migrations/
│
├── analytics/                     # Analytics & reporting
│   ├── views.py                  # Analytics endpoints
│   ├── serializers.py            # Data serialization
│   ├── urls.py                   # Analytics URLs
│   └── utils.py                  # Helper functions
│
├── templates/                     # Django templates (Template version)
│   ├── base.html                 # Base template
│   ├── auth/
│   ├── dashboard/
│   ├── expenses/
│   ├── budgets/
│   └── components/
│
├── static/                        # Static files
│   ├── css/
│   ├── js/
│   ├── images/
│   └── icons/
│
├── frontend/                      # React frontend (DRF version)
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── context/               # State management
│   │   ├── api/                   # API calls
│   │   ├── styles/
│   │   └── App.js
│   ├── package.json
│   └── README.md
│
├── docs/                          # Documentation
│   ├── API.md                    # API documentation
│   ├── SETUP.md                  # Setup guide
│   ├── CONTRIBUTING.md           # Contributing guidelines
│   └── ARCHITECTURE.md           # Architecture details
│
└── tests/                         # Integration & E2E tests
    ├── test_integration.py
    └── test_e2e.py
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)
- Git

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/expense_tracker_with_DRF_and_templates.git
   cd expense_tracker_with_DRF_and_templates
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   ```bash
   # Copy example file
   cp .env.example .env
   
   # Edit .env with your configuration
   ```

5. **Database Setup**
   ```bash
   # Create and apply migrations
   python manage.py makemigrations
   python manage.py migrate
   
   # Create superuser for admin panel
   python manage.py createsuperuser
   
   # Load sample data (optional)
   python manage.py loaddata fixtures/sample_data.json
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```
   - Backend (DRF): http://localhost:8000/api/
   - Admin Panel: http://localhost:8000/admin/

### Frontend Setup (DRF Version)

```bash
cd frontend
npm install
npm start
```

Frontend will run on: http://localhost:3000/

---

## 📚 API Documentation

### Authentication Endpoints

```
POST   /api/auth/register/          - User registration
POST   /api/auth/login/             - User login (returns JWT token)
POST   /api/auth/logout/            - User logout
POST   /api/auth/refresh/           - Refresh JWT token
GET    /api/auth/profile/           - Get user profile
PUT    /api/auth/profile/           - Update user profile
```

### Expense Endpoints

```
GET    /api/expenses/               - List all expenses (paginated)
POST   /api/expenses/               - Create new expense
GET    /api/expenses/{id}/          - Get expense details
PUT    /api/expenses/{id}/          - Update expense
DELETE /api/expenses/{id}/          - Delete expense
GET    /api/expenses/filter/        - Filter expenses (date, category, amount)
GET    /api/categories/             - List all expense categories
```

### Budget Endpoints

```
GET    /api/budgets/                - List all budgets
POST   /api/budgets/                - Create new budget
GET    /api/budgets/{id}/           - Get budget details
PUT    /api/budgets/{id}/           - Update budget
DELETE /api/budgets/{id}/           - Delete budget
GET    /api/budgets/status/         - Get budget vs. actual spending
```

### Analytics Endpoints

```
GET    /api/analytics/summary/      - Get spending summary
GET    /api/analytics/trends/       - Get spending trends
GET    /api/analytics/categories/   - Get category breakdown
GET    /api/analytics/comparison/   - Compare periods
```

**Full API Documentation:** See [API.md](docs/API.md) for detailed endpoints and request/response examples.

---

## 🔧 Configuration

### Environment Variables (.env)

```env
# Django Configuration
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# For PostgreSQL (Production)
# DB_ENGINE=django.db.backends.postgresql
# DB_HOST=localhost
# DB_PORT=5432
# DB_NAME=expense_tracker
# DB_USER=postgres
# DB_PASSWORD=your-password

# JWT Configuration (DRF)
JWT_SECRET=your-jwt-secret
JWT_ALGORITHM=HS256

# CORS Configuration (DRF with separate frontend)
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Email Configuration (for notifications)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

See [.env.example](.env.example) for all available options.

---

## 🧪 Testing

### Run All Tests
```bash
python manage.py test
```

### Run Specific App Tests
```bash
python manage.py test accounts
python manage.py test expenses
python manage.py test budgets
```

### Generate Coverage Report
```bash
coverage run --source='.' manage.py test
coverage report
coverage html  # Opens htmlcov/index.html
```

---

## 📱 Responsive Design

The application is optimized for:
- ✅ Mobile (320px and up)
- ✅ Tablet (768px and up)
- ✅ Desktop (1024px and up)

All views adapt seamlessly across device sizes.

---

## 🚢 Deployment

### Heroku Deployment
```bash
# Create Procfile
echo "web: gunicorn config.wsgi" > Procfile

# Create runtime.txt
echo "python-3.10.5" > runtime.txt

# Deploy
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Docker Deployment
```bash
# Build image
docker build -t expense-tracker .

# Run container
docker run -p 8000:8000 expense-tracker
```

See [SETUP.md](docs/SETUP.md) for detailed deployment guides.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## 📊 Project Status

### ✅ Completed
- [x] Project setup & Django configuration
- [x] Database models (User, Expense, Budget, Category)
- [x] User authentication system
- [x] Basic API endpoints
- [x] Template-based views

### 🔄 In Progress
- [ ] Advanced filtering & search
- [ ] Analytics dashboard
- [ ] React frontend integration
- [ ] Chart visualizations
- [ ] Budget alert system

### 📅 Planned
- [ ] Currency converter
- [ ] Recurring expenses
- [ ] PDF/CSV export
- [ ] Email notifications
- [ ] Mobile app (React Native)
- [ ] Dark mode
- [ ] Multi-language support

---

## 🔒 Security Considerations

- ✅ Password hashing using Django's built-in system
- ✅ CSRF protection on forms
- ✅ SQL injection prevention via ORM
- ✅ XSS protection with template auto-escaping
- ✅ Secure JWT token management (DRF)
- ✅ CORS configuration for separate frontend
- ✅ Environment variable protection
- ✅ Rate limiting on API endpoints (coming soon)

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 👥 Team Structure

This project is designed for a student team with the following roles:

- **Backend Developer:** Django REST Framework APIs, database design, authentication
- **Frontend Developers (2):** React dashboard, forms, charts, state management
- **UI/UX Designer:** Responsive layouts, visual design, component design
- **HTML Developer:** Static pages, landing page, accessibility
- **QA Engineer:** Testing, bug reporting, quality assurance

---

## 📚 Learning Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Guide](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [Recharts Documentation](https://recharts.org/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

---

## 🙋 FAQ

**Q: Can I use PostgreSQL in development?**  
A: Yes! Update `DB_ENGINE` in `.env` to use PostgreSQL.

**Q: How do I reset the database?**  
A: Run `python manage.py flush` then `python manage.py migrate`.

**Q: Where are the API docs?**  
A: Navigate to `/api/docs/` or `/api/swagger/` (when implemented).

**Q: How do I add a new expense category?**  
A: Use the admin panel at `/admin/` or via the API.

---

## 📞 Support & Contact

For issues, questions, or suggestions:
- 📧 Email: your-email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/expense_tracker_with_DRF_and_templates/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/expense_tracker_with_DRF_and_templates/discussions)

---

## 🙏 Acknowledgments

- Django and DRF communities for excellent documentation
- Recharts for data visualization
- The SDLC Project team for clear requirements and vision

---

**Happy coding! 🚀**

*Last Updated: February 2026*
