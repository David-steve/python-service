"""
@Project: python-service
@File: manage.py
@Author: David
@Date: 2025/6/4
@Brief: 
"""
# !/usr/bin/env python
import os
import sys
from django.conf import settings

import django

if not settings.configured:
    sys.dont_write_bytecode = True

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.orm.settings')
    django.setup()


def migrate(model):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(["manage.py", "makemigrations", model])
    execute_from_command_line(["manage.py", "migrate", model])


if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    # from django.core.management import execute_from_command_line
    #
    # execute_from_command_line(["manage.py", "makemigrations", "models"])
    # execute_from_command_line(["manage.py", "migrate", "models"])
    migrate('db')
    pass
