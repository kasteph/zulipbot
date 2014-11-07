import os
import zulipbot

# I initialize the bot
my_bot = zulipbot.Bot(os.environ['ZULIP_EMAIL'], os.environ['ZULIP_KEY'])

# Then make it to subscribe to all the streams (this is optional)
my_bot.subscribe_to_all_streams()


def process_message(message):
    '''
    process_message(message) -> <message> is a dictionary of meta-info
    about the message(s) from streams or people that the bot listens to.

    Where the main functionality of your bot goes. This function will be
    passed as a callback function to Bot.call_on_each_message(<func>).
    '''
    content = message['content'].split()
    sender_email = message['sender_email']

    if sender_email == os.environ['ZULIP_EMAIL']:
        return

    if content[0] == 'test':
        if message['type'] == 'stream':
            my_bot.send_stream_message(message, 'Stream message')
        else:
            my_bot.send_private_message(message, 'Private message')


# This runs forever!
my_bot.call_on_each_message(process_message)
