import yaml
from yaml import Loader

def get_config(config_path):
    with open(config_path, 'r') as stream:
        config = yaml.load(stream, Loader)
    return config