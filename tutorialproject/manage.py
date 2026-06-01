#!/usr/bin/env python  # Specifies the interpreter to execute this script under Unix-like systems
"""Django's command-line utility for administrative tasks."""                    # Module-level docstring describing the script's purpose

# we'd use this file to run the server and other management commands, such as migrations, creating superusers, etc. It sets the default settings module to 'core.settings'

import os                    # Imports built-in os module, outputs/returns the module namespace object (E.g., <module 'os' from '...'>)
import sys                    # Imports built-in sys module to access CLI parameters, outputs the module namespace object (E.g., <module 'sys' (built-in)>)


def main():                    # Defines main admin entrypoint function, executes administrative commands and outputs None (E.g., None)
    """Run administrative tasks."""                    # Function docstring explaining purpose
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')                    # Sets environment settings variable, outputs string value 'core.settings' (E.g., 'core.settings')
    try:                    # Begins exception block to verify package installation, outputs control flow direction
        from django.core.management import execute_from_command_line                    # Imports CLI execution runner, outputs a callable function (E.g., <function execute_from_command_line at 0x...>)
    except ImportError as exc:                    # Catches ImportError if django is missing, outputs exception instance 'exc' (E.g., ImportError("No module named 'django'"))
        raise ImportError(                    # Instantiates and raises ImportError containing customized instruction string
            "Couldn't import Django. Are you sure it's installed and "                    # Custom error message part 1
            "available on your PYTHONPATH environment variable? Did you "                    # Custom error message part 2
            "forget to activate a virtual environment?"                    # Custom error message part 3
        ) from exc                    # Links original cause 'exc' to current raised exception, outputting traceback
    execute_from_command_line(sys.argv)                    # Runs command task using list string arguments from 'sys.argv' (E.g., ['manage.py', 'runserver']), outputs CLI task results or raises SystemExit


if __name__ == '__main__':                    # Evaluates whether the script is run directly, outputs/evaluates to a boolean (E.g., True)
    main()                    # Invokes main() defined above, starting processing and outputting None (E.g., None)
