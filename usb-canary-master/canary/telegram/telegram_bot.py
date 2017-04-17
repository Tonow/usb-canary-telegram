try:
    import telepot
except ImportError, e:
    if e.message != 'No module named telepot':
        pass

import sys

telegram_server = None
id_client = None


def setup(telegram, client):
    '''
    No setup doing for this moment
    '''

def run_bot(message, id_client, bot_token):

    bot = telepot.Bot(bot_token)
    bot.sendMessage(id_client, message)
