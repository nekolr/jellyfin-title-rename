import config


class JellyfinApi(object):
    def __init__(self):
        cf = config.Config()
        self.api_key = cf.jellyfin['api_key']
        self.base_url = cf.jellyfin['base_url']
        self.user_id = cf.jellyfin['user_id']
        self.version = cf.jellyfin['version']

    def get_items(self):
        pass

    def get_user_library_item(self, item_id):
        pass

    def update_item(self, item):
        pass

    def print_version(self):
        print('Support Jellyfin Server Version: ' + self.version)
