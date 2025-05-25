# 📰 Blog API

A robust and scalable Blog API built using Django and Django REST Framework (DRF). This project provides endpoints for managing blog posts, categories, and user authentication, facilitating seamless integration with frontend applications or third-party services.

## 🚀 Features

- **User Authentication**: Secure user registration and login functionalities.
- **Post Management**: Create, retrieve, update, and delete blog posts.
- **Category Management**: Organize posts into categories for better content management.
- **Permissions**: Implemented permissions to control access to various endpoints.
- **Pagination**: Efficiently handle large datasets with paginated responses.
- **Filtering & Search**: Easily filter and search through posts and categories.

## 🛠️ Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default, can be switched to PostgreSQL or others)
- **Authentication**: Token-based authentication using DRF's built-in mechanisms

## 📁 Project Structure

blog_api/
├── blog/ 
├── BlogApp/ 
├── db.sqlite3 
├── manage.py 
├── requirement.txt
└── README.md 


## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/promisenmor/blog_api.git
   cd blog_api
python -m venv venv
source venv/bin/activate  

pip install -r requirement.txt

python manage.py runserver

Access the API:
Navigate to http://127.0.0.1:8000/api/ in your web browser or use tools like Postman to interact with the endpoints.

## 📌 Future Enhancements
Implementing JWT authentication for enhanced security.

Adding support for comments on blog posts.

Integrating Swagger or ReDoc for interactive API documentation.

Deploying the application to cloud platforms like Heroku or AWS.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

