import zulip
import requests


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
        return requests.get(endpoint, auth=requests.HTTPBasicAuth(self._email, self._key))

    def subscribe_to_all_streams(self):
        '''Subscribe to all Zulip streams.'''
        zulip_streams = self.zulip_api + '/streams'
        print zulip_streams
        response = self._zulip_request(zulip_streams)

        if response.status_code == 200:
            json = response.json()['streams']
            streams = [{'name': stream['name']} for stream in json]
            self.add_subscriptions(streams)
        else:
            raise Exception(response)

    def get_subscriptions(self):
        '''Get list of joined streams.'''
        joined_streams = self.zulip_api + '/users/me/subscriptions'
        response = self._zulip_request(joined_streams)

        return response
