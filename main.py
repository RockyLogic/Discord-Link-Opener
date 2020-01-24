#Libraries Required
import discord
import re
import datetime
import webbrowser
import asyncio


token = ""
client = discord.Client()

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
    if message.channel.id in channelList:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
        if urls:
            print (f"[{datetime.datetime.now()}] Link(s) Found:")
            for x in range(len(urls)):
                print(urls[x])
                await open_url(urls[x])
                
                
async def open_url(url):
    webbrowser.get("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s").open(url)
    print ("test")  
                

client.run(token, bot=False)
            
        