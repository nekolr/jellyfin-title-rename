import json
import requests
import logging
from jellyfin.api import JellyfinApi


class JellyfinClient(JellyfinApi):

    def get_items(self):
        get_items_uri = '/Items'
        headers = {'X-Emby-Token': self.api_key}
        params = {'userId': self.user_id, 'parentId': '95cbbc4f2abf600398bc7836bd5a5e7b'}
        resp = requests.get(self.base_url + get_items_uri, headers=headers, params=params)
        return json.loads(resp.text)['Items'] if resp.status_code == 200 else []

    def get_user_library_item(self, item_id):
        get_user_library_item_uri = '/Users/{UserId}/Items/{ItemId}'.format(UserId=self.user_id, ItemId=item_id)
        headers = {'X-Emby-Token': self.api_key}
        resp = requests.get(self.base_url + get_user_library_item_uri, headers=headers)
        return json.loads(resp.text) if resp.status_code == 200 else []

    def update_item(self, item):
        update_item_uri = '/Items/{ItemId}'.format(ItemId=item.Id)
        headers = {'X-Emby-Token': self.api_key}
        # headers = {'X-Emby-Token': self.api_key, 'Content-Type': 'application/json'}
        # resp = requests.post(self.base_url + update_item_uri, headers=headers, data=json.dumps(item.__dict__))
        resp = requests.post(self.base_url + update_item_uri, headers=headers, json=item.__dict__)
        logging.info("update item response: %s", resp)
        return resp.status_code == 204
