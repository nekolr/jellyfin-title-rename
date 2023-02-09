import configparser


class Config(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.peashooter = {
            'base_url': config['peashooter']['baseUrl'],
            'api_key': config['peashooter']['apiKey']
        }

        self.jellyfin = {
            'base_url': config['jellyfin']['baseUrl'],
            'api_key': config['jellyfin']['apiKey'],
            'user_id': config['jellyfin']['userId'],
            'version': config['jellyfin']['version']
        }
