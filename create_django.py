import os
import subprocess


def create_django():
    """
     Automates the process of setting up a Django project.

    This function activates the virtual environment and runs essential
    Django commands including makemigrations, migrate, and runserver.

    It does not take any parameters.

    The function performs the following steps:
    1. Sets the project path to the specified Django project directory.
    2. Retrieves the path to the Python interpreter within the virtual environment.
    3. Defines the Django commands to be executed.
    4. Executes each command in the order they are defined.

    Example usage:
        create_django()

    Note:
        Ensure that the specified project path exists and contains a valid
        Django project with a manage.py file and a properly set up virtual
        environment.
    """

    # project_path = os.path.expanduser("/home/jahongir/Downloads/Telegram Desktop/online_shoping")
    project_path = os.path.dirname(os.path.abspath(__file__))
    venv_python = os.path.join(project_path, "venv/bin/python")

    commands = [
        [venv_python, "manage.py", "makemigrations"],
        [venv_python, "manage.py", "migrate"],
        [venv_python, "manage.py", "runserver"]
    ]

    for command in commands:
        subprocess.run(command, cwd=project_path)


create_django()
