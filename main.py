#Libraries Required
import discord
import re
import datetime

token = "Token"
client =discordClient()

def getChannelIDs():
    channelList = []
    with open ("channel ID.txt", "r") as file:
        for id in file:
            channelList.append(int(id.strip()))
    return channelList

channelList = getChannelIDs()

@client.event
async def on_ready():
    print (f"[{datetime.datetime.now()}] Link Opener Ready!")
    print (f"[{datetime.datetime.now()}] Channels Loaded:")
    for x in range(len(channelList)):
        print(channelList[x])
    
    
@client.event
async def on_message(message):
    if message.channel in channelList:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
        if urls:
            print (f"[{datetime.datetime.now()}] Link(s) Found:")
            for x in range(len(urls)):
                print(urls.group())
                
                

client.run(token)
            
        