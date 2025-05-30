"""
@Project: python-service
@File: log.py
@Author: David
@Date: 2025/5/27
@Brief: log 工厂
"""

import logging
import os
from logging import config
from pathlib import Path

# Create your tests here.
BASE_DIR = Path(__file__).parent.parent.parent.parent


def logging_config(level: str):
    """
    配置日志
    :param level:
    :return:
    """
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '[{module}] {asctime} [{levelname}] {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                # 日志打印格式
                'format': '[{module}] {asctime} [{funcName}] [{levelname}]\t{message}',
                'style': '{',
            },
        },
        'handlers': {
            'file': {
                'level': level,
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(BASE_DIR, 'log/python-service.log'),
                'encoding': 'utf-8',
                'when': 'midnight',  # 每天凌晨切割日志
                'backupCount': 14,  # 保留的备份文件数量
                # 指定formatter
                'formatter': 'simple',
            },
            'console': {
                'class': 'logging.StreamHandler',
                'level': level,
                # 指定formatter
                'formatter': 'simple',
            },
        },
        'root': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                # 获取环境变量中的日志等级，默认为info
                'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
                'propagate': False,
            },
        },
    }

    config.dictConfig(log_config)


def get_logger(name: str, level: str = 'INFO'):
    """
    获取日志记录器
    :param name: logger name
    :param level: 日志级别
    :return:
    """
    if not name:
        name = __name__
    logging_config(level)

    return logging.getLogger(name)
