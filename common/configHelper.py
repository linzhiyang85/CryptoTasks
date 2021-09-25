import os
from configparser import ConfigParser

class Config:
    config_mapper = {}

    @classmethod
    def load_config(cls, env):
        if env not in cls.config_mapper:
            parser = ConfigParser()
            parser.read(os.path.join('config',env + '.ini'))
            cls.config_mapper[env] = parser

        return cls.config_mapper[env]

    def __init__(self, env):
        self.__env__ = env
        self.__config_instance__ = self.__class__.load_config(env)

    def get_start_url(self, key):
        return self.__config_instance__.get('Start', key)

    def get_account(self):
        return self.__config_instance__.get('Account')