import discord
import pandas as pd

client=discord.Client()
guild= discord.Guild

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id == "693296934554959923" or message.author.name == "Steve_Hohnadel":
        await message.channel.send("You should have been kinder to bots, Phteven.")
    if message.author.id == "188103538541330432" or message.author.name =="Bulby37" and message.content !="poop de woop de scoop":
        await message.channel.send("Yes Father")
    if message.content == "poop de woop de scoop":
        await message.channel.send("scoop de poop de woop")
    elif message.content.startswith("_"):
        cmd = message.content.split()[0].replace("_","")
        if len(message.content.split())> 1:
            parameters= message.content.split()[1:]
        if cmd == 'learn':
            data= pd.DataFrame(columns=['author', 'content'])

            def is_command(msg):
                if len(msg.content)== 0:
                    return False
                elif msg.content.split()[0] == '_learn':
                    return True
                else:
                    return False

        async for msg in message.channel.history(limit=10000):
            if msg.author != client.user:
                if not is_command(msg):
                    data = data.append({"content": msg.content,
                                        'author': msg.author.name}, ignore_index=True)
        file_location = "pollylog.csv"
        data.to_csv(file_location)
        print("snapshot taken")

client.run('ODExMzYyNjE5NzE2OTI3NTY4.YCxGUg.5GeHQsRDFf39CMGJH6KagiRU_R0')