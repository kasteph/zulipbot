import zulip
import requests
from requests.auth import HTTPBasicAuth


class Bot(zulip.Client):
    def __init__(self, email, key):
        '''
        Bot(email, key) ->
        email and key can be retrieved under settings
        when you've generated a new bot on Zulip.
        '''
        self._email = email
        self._key = key
        self.zulip_api = 'https://api.zulip.com/v1'
        super(Bot, self).__init__(self._email, self._key)

    def _zulip_request(self, endpoint):
        '''A generic zulip request.'''
        return requests.get(endpoint, auth=HTTPBasicAuth(self._email, self._key))

    def subscribe_to_all_streams(self):
        '''Subscribe to all Zulip streams.'''
        zulip_streams = self.zulip_api + '/streams'
        response = self._zulip_request(zulip_streams)

        if response.status_code == 200:
            json = response.json()['streams']
            streams = [{'name': stream['name']} for stream in json]
            self.add_subscriptions(streams)
        else:
            raise Exception(response)

    def send_private_message(self, message_info, content):
        self.send_message({
            'type': 'private',
            'to': message_info['sender_email'],
            'content': content
        })

    def send_stream_message(self, message_info, content):
        self.send_message({
            'type': 'stream',
            'subject': message_info['subject'],
            'to': message_info['display_recipient'],
            'content': content
        })
