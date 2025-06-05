"""
@Project: python-service
@File: settings.py
@Author: David
@Date: 2025/6/4
@Brief: django settings
"""
import os
from pathlib import Path

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"
TIME_ZONE = 'Asia/Shanghai'

# 自动递增
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
DEFAULT_CHARSET = 'utf-8'

BASE_DIR = Path(__file__).parent

DATABASES = {
    'free': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'connect_timeout': 9,  # 连接超时时间
            'charset': 'utf8mb4',
            'read_default_file': os.path.join(BASE_DIR, './free_db.cnf'),
        },
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'connect_timeout': 9,  # 连接超时时间
            'charset': 'utf8mb4',
            'read_default_file': os.path.join(BASE_DIR, './default_db.cnf'),
        },
    }
}

INSTALLED_APPS = (
    "src.finance",
)
