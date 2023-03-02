import discord

import os
from gpt_index import GPTSimpleVectorIndex
from dotenv import load_dotenv
load_dotenv()

MYAPI = os.getenv('MYAPI')
# THEURL = os.getenv('THEURL')
QUESTION1 = os.getenv('QUESTION1')
DISCORDTOKEN = os.getenv('DISCORDTOKEN')

os.environ["OPENAI_API_KEY"] = MYAPI
json_path = "./data/wiki.json"
 
index = GPTSimpleVectorIndex.load_from_disk(json_path)
 
# print(index.query("聖書の内容を要約してください。？"))
# print(index.query(QUESTION1))


# インテントの生成
intents = discord.Intents.default()
intents.message_content = True

# クライアントの生成
client = discord.Client(intents=intents)

# discordと接続した時に呼ばれる
@client.event
async def on_ready():
    print('We have logged in as {client.user}')

# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
    # 自分のメッセージを無効
    if message.author == client.user:
        return

    # メッセージが"$hello"で始まっていたら"Hello!"と応答
    if message.content.startswith('$hello'):
        # print(message.content)
        # print(index.query(message.content))
        await message.channel.send('Hello! I am coffin. Thank you for calling me!')

    if message.content.startswith('$coffin'):
        # print(message.content)
        print(index.query(message.content))
        await message.channel.send(index.query(message.content))
        # await message.channel.send("message")
        # await message.channel.send('Hello!')
        return

    else:
        return

# クライアントの実行
client.run(DISCORDTOKEN)
