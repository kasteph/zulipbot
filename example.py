import os
import zulipbot

my_bot = zulipbot.Bot(os.environ['ZULIP_EMAIL'], os.environ['ZULIP_KEY'])
print my_bot
my_bot.send_message({
        'type': 'stream',
        'to': 'bot-test',
        'subject': 'hello',
        'content': 'I work!'
    })

my_bot.subscribe_to_all_streams()
print my_bot.get_subscriptions()


def process_message(msg):
    content = msg['content'].split()
    sender_email = msg['sender_email']

    if sender_email == os.environ['ZULIP_EMAIL']:
        return

    if content[0] == 'test':
        if msg['type'] == 'stream':
            my_bot.send_message({
                'type': 'stream',
                'subject': msg['subject'],
                'to': msg['display_recipient'],
                'content': 'YAY!'
            })
        else:
            my_bot.send_message({
                'type': 'private',
                'to': msg['sender_email'],
                'content': 'WOOT'
            })

my_bot.call_on_each_message(process_message)
