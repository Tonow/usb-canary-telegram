import telepot
import sys

telegram_server = None
id_client = None


def setup(telegram, client):
    '''
    global telegram_server
    telegram_server = telepot.Bot.getMe(telegram['bot_token'])
    global id_client
    id_client = client
    '''
    #print('setup ok')

def run_bot(message, id_client, bot_token):

    bot = telepot.Bot(bot_token)
    bot.sendMessage(id_client, message)
