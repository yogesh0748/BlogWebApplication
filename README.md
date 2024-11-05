# Blogging Web Application in Django

This is a simple blogging web application built using **Django**, a popular Python web framework. The app allows users to create, read, update, and delete blog posts. It also includes user authentication and basic features for managing posts, comments, and categories.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Blog Post Management**: Users can create, edit, delete, and view blog posts.
- **Categories**: Organize posts into categories for easier browsing.
- **Comments**: Users can leave comments on blog posts.
- **Admin Panel**: Easy management of blog posts, categories, and comments via Django's built-in admin interface.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **HTML/CSS**: For basic page structure and styling.
- **SQLite**: Default database for the app (can be switched to other databases like PostgreSQL).
- **Bootstrap**: A CSS framework for responsive design (optional, if included).

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/blogging-app.git
    cd blogging-app
    ```

2. **Set up a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (to access the Django admin panel):

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up your admin credentials.

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000/` in your browser to view the application.
8. Visit `http://127.0.0.1:8000/home` in your browser to view the application.
9. Visit `http://127.0.0.1:8000/admin` in your browser to view the application.
## Usage

- **Login/Register**: Users can create an account or log in to manage their blog posts.
- **Create a Post**: After logging in, users can create new blog posts with a title, body content, and category.
- **View Posts**: All blog posts are displayed on the home page and can be filtered by category.
- **Commenting**: Authenticated users can leave comments on blog posts.
- **Admin Panel**: The Django admin interface is available at `/admin` for managing posts, categories, and comments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this repository and submit pull requests for improvements. Please follow best practices for code formatting and testing.

## Acknowledgments

- **Django**: For the powerful web framework that makes web development easy.
- **Bootstrap**: For responsive and user-friendly design components.
- **SQLite**: For the lightweight database used in development.
