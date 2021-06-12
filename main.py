from telethon import TelegramClient, sync, utils
import asyncio, datetime,configparser

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
# api_id = 0
# api_hash = ''
#init
config = configparser.ConfigParser()
config.read('base-config.ini')
api_id = config.get('client', 'api_id')
api_hash = config.get('client', 'api_hash')
target_group = config.get('group', 'target_group')
foward_group = config.get('group', 'foward_group')
target_ids = config.get('group', 'target_ids')

client = TelegramClient('session_name', api_id, api_hash)
client.start()
#create a listener
loop = asyncio.get_event_loop()

async def main(target_group, foward_group):
    #get messages from speci username
    channel_records = await client.get_entity(target_group)
    #userNameList = ['mkhsieh', 'LoveG_G', 'miulahung']
    # userIds = [521521130, 1104929860, 1056919703]
    date_of_post = datetime.datetime(2020, 6, 6)
    # reverse = True -> From oldest to most-recent
    async for message in client.iter_messages(channel_records, offset_date = date_of_post, reverse = True):
        #Filter message by sender_id
        if(target_ids):
            if (str(message.sender_id) in list(str(target_ids).split(","))):
                # print(str(message.sender_id) + '->' + str(message.text))
                # forward_messages to privet group
                await client.forward_messages(entity= foward_group, messages = message)

loop.run_until_complete(main(target_group, foward_group))