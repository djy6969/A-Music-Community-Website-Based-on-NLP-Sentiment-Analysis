from router import *
from app import manager
from flask_script import Server

manager.add_command("runserver", Server('0.0.0.0', port=5000))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exception()