# -*- coding: utf-8 -*-

import os
from ckan.config.middleware import make_app
from ckan.cli import CKANConfigLoader
import logging
from logging.config import fileConfig as loggingFileConfig

config_filepath = os.path.join(u'/etc/ckan/config.ini')
# config_filepath = os.path.join(
#     os.path.dirname(os.path.abspath(__file__)), u'contrib/docker/dev.ini')
abspath = os.path.join(os.path.dirname(os.path.abspath(__file__)))
# loggingFileConfig(config_filepath)
config = CKANConfigLoader(config_filepath).get_config()
application = make_app(config)

#loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict if '.' not in name]
loggers = [logging.getLogger(name) for name in ['ckan', 'ckanext', 'universal_analytics']]
for log in loggers:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    log.handlers = gunicorn_logger.handlers
    log.setLevel(gunicorn_logger.level)
