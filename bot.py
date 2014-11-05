import zulip
import requests


class Bot(object):
    def __init__(self, email, key):
        '''
        Bot(email, key) ->
        email and key can be retrieved under settings
        when you've generated a new bot on Zulip.
        '''
        self._email = email
        self._key = key
        self.client = zulip.Client(self._email, self._key)

    def subscribe_all(self):
        '''Subscribe to all Zulip streams.'''
        streams = 'https://api.zulip.com/v1/streams'
        response = requests.get(streams, auth=requests.auth.HTTPBasicAuth(self._email, self._key))

        if response.status_code == 200:
            json = response.json()['streams']
            streams = [{'name': stream['name']} for stream in json]
            self.client.add_subscriptions(streams)
        else:
            raise Exception(response)
