from telethon import TelegramClient, sync, utils
import asyncio, datetime

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 4190078
api_hash = '1b8b4ebef76ebd1a2f469884694d2940'
#init
client = TelegramClient('session_name', api_id, api_hash)
client.start()
#create a listener
loop = asyncio.get_event_loop()

async def main():
    #get messages from speci username
    gooaye_us_group = 'https://t.me/joinchat/HxXH6kP61QnYrME9TbgGeQ'
    channel_records = await client.get_entity(gooaye_us_group)
    
    
    #userNameList = ['mkhsieh', 'LoveG_G', 'miulahung']
    #userIds = [521521130, 1104929860, 1056919703]
    date_of_post = datetime.datetime(2020, 6, 6)
    # reverse = True -> From oldest to most-recent
    async for message in client.iter_messages(channel_records, offset_date = date_of_post, reverse = True):
        #Filter message by sender_id
        if (message.sender_id in [521521130, 1104929860, 1056919703]):
            # print(str(message.sender_id) + '->' + str(message.text))
            # forward_messages to privet group
            us_backup_group = 'https://t.me/joinchat/-o6RjFkK6FxkZDFl'
            await client.forward_messages(entity= us_backup_group, messages = message)

        # SOLUSUTION 2
        # if (str(message.from_id).replace("PeerUser(user_id=", "").replace(")", "") == "521521130"):
        # # input_peer = PeerUser(message.from_id,  mk.access_hash)
        #     print('mk: ' + str(message.from_id) + '->' + str(message.text))

loop.run_until_complete(main())