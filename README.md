# Feast of Features: Building Your First Thanksgiving API with FastAPI 🦃

Welcome to GDG on Campus @ Tulane's hands-on workshop where you'll build your first API endpoint! We're creating a Thanksgiving-themed potluck API to manage dishes that Tulane students are bringing to the celebration.

## 📝 Before We Start: Database Setup

⚠️ **Important: Do not clone the repository yet!** ⚠️

As the workshop host, I'll first populate our in-memory database with your suggestions:

1. Share your favorite Thanksgiving/potluck dish ideas with me
2. I'll add them to the `database.py` file
3. Once all entries are added, I'll push the changes
4. Then you can proceed with cloning the repository

### Understanding In-Memory Database

This workshop uses an in-memory database (a Python list in `database.py`) to keep things simple. Here's what you need to know:

- The initial data is stored in the code (`database.py`)
- When you use POST/PATCH/DELETE endpoints:
  - Changes are only kept in memory while the server runs
  - Changes won't be saved back to the `database.py` file
  - Restarting the server will reset to the initial data
- In real-world applications:
  - Changes would persist to a real database (like PostgreSQL, MongoDB)
  - Data would remain even after server restarts
  - Multiple users could see each other's changes

## 🎯 Workshop Goals

- Learn the basics of REST API development using FastAPI
- Understand CRUD operations (Create, Read, Update, Delete)
- Practice Git workflow in a team setting
- Test API endpoints using FastAPI's built-in documentation

## 🚀 Getting Started

### 1. Setup Your Development Environment

```bash
# Clone the repository
git clone https://github.com/tpthanh2006/tulane-gdgc-build-your-first-api.git
cd tulane-gdgc-build-your-first-api

# Create a new branch for your feature
git checkout -b your-feature-name

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Verify Your Setup

```bash
# Run the FastAPI server
fastapi dev main.py

# Visit the welcome page in your browser
# You should see the welcome message at localhost:8000
```

## 📝 Workshop Tasks

### Task 1: Choose Your API Endpoint

Pick one of the following endpoints to implement:

1. **GET /potluck** - Retrieve all potluck dishes
2. **GET /potluck/{dish_id}** - Get a specific dish by ID
3. **POST /potluck** - Add a new dish
4. **PATCH /potluck/{dish_id}** - Update a dish
5. **DELETE /potluck/{dish_id}** - Remove a dish

### Task 2: Implement Your Endpoint

- Remove the `pass` statement in your chosen function
- Implement the functionality following the comments
- Test your endpoint using FastAPI's built-in documentation interface

### Important Notes

- We're using an in-memory database (list in `database.py`)
- Changes to the database won't persist after server restart
- Database modifications will only be visible in API responses

## 🧪 Testing Your API

### Using FastAPI Docs (Swagger UI)

1. Start your server: `fastapi dev main.py`
2. Open your browser and navigate to the docs interface at localhost:8000/docs
3. Find your endpoint in the documentation
4. Click "Try it out" to test

### Using Postman (Industry Standard)

- While we'll use FastAPI's built-in docs for this workshop, Postman is the industry standard
- [Watch this Postman tutorial](https://www.youtube.com/watch?v=CLG0ha_a0q8&pp=ygUiaG93IHRvIHVzZSBwb3N0bWFuIGZvciBhcGkgdGVzdGluZw%3D%3D) to learn more

## 📤 Submitting Your Work

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m 'feat: implement get all dishes endpoint'

# Push to your branch
git push --set-upstream origin your-feature-name

# Create a Pull Request on GitHub
# Wait for review and feedback
```

## 🔍 Code Review Process

1. Other teams will review your PR
2. Address any feedback
3. Once approved, your code will be merged into the main branch

## 🌟 Extra Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [RESTful API Design Guidelines](https://restfulapi.net/)
- [Git Workflow Best Practices](https://www.atlassian.com/git/tutorials/comparing-workflows)
