# Todo List Web Application Manager

This is a simple Flask-based web application for managing personal todo lists. Users can create multiple todo lists, add tasks to each list, mark tasks as completed, delete tasks, and edit list titles. The app tracks progress by showing the number of remaining todos and provides a clean, session-based interface for task management.

## Features

- **Manage Multiple Todo Lists**: Add, view, edit, or delete todo lists.
- **Task Management**: Add, mark as complete/incomplete, or delete tasks in a list.
- **Progress Tracking**: Displays remaining tasks in each list.
- **Sorting**: Todo lists are sorted by completion status and title.
- **Session-Based Storage**: Data is stored temporarily in user sessions.

## Prerequisites

- Python 3.7+
- Flask
- Poetry

### Installation

1. Clone this repository:

    ```console
    git clone https://github.com/Spicyblue/Todo_App.git
    ```


2. Install Dependencies:  
    Necessary dependencies includes Poetry, Flasks and Python(Version 3.9 and above) The application was developed using python3.12

    To install Poerty, first install pipx and then poetry by using the following command on your commandline interface

    ```console
    pip install pipx
    pipx install poetry
    pip install flask
    ```

    Once Poetry is installed, run the code below to install the project dependencies

    ```console
    poetry lock
    poetry install
    ```

3. Set up the file structure:

    app.py: Main flask application.
    wsgi.py: Web Server Gateway Interface entry point file.
    pyproject.toml: Configuration file.
    todos: Contains helper functions for validations
    templates: Contains all necessary HTML templates.
    static: Contains all static files.

4. Run the application

    To run the application, ensure you are in the directory for book_viewer containing app.py
    Next, run the following code on your commandline interface.

    ```console
    poetry run python app.py
    ````

    Open your application in your broswer by entering the address below:
    http://localhost:5003

### License

This project is open-source and licensed under the MIT License. Feel free to use and adapt it for your own projects. See License.md for more infomation about the license
