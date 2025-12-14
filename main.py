import configparser
from telethon import TelegramClient
from get_jokes import Jokes
import asyncio

# Parsing settings.ini
config = configparser.ConfigParser()
config.read('settings.ini')

# Getting tg info
api_id = int(config['TG']['api_id'])
api_hash = config['TG']['api_hash']
user_tg_id = int(config['TG']['user_id'])

session_name = 'anon'

#Action selection
print('Select an option:' )
print('1 - Send jokes' )
print('2 - Send smth else' )
print('3 - Add users' )
print('4 - Delete users' )
print('5 - Close the program')
selection = input()

if selection == '1':
    #Count of jokes
    jokes_count = input('Print count of jokes(1, 5, 10, 20, 30, 50, 100): ')

    #Printing jokes
    jokes = Jokes(jokes_count)

    # Sending jokes
    async def main():
        await client.start()
        await client.send_message('@stolen_overcoat', 'ВНЕЗАПНАЯ РУБРИКА "АНЕКДОТЫ"!!!!')
        await client.send_message('@stolen_overcoat', await jokes.filtering())
        print(await jokes.filtering())


    if __name__ == '__main__':
        with TelegramClient(session_name, api_id, api_hash) as client:
            client.loop.run_until_complete(main())

elif selection == '2':
    #Need to send pictures
    #Sending
    async def main():
        text = input('Send: ')
        await client.start()
        await client.send_message('@stolen_overcoat', text)


    if __name__ == '__main__':
        with TelegramClient(session_name, api_id, api_hash) as client:
            client.loop.run_until_complete(main())
