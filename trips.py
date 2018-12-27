import discord
client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Fuck you"))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Fuck you":
        await client.send_message(message.channel, "Bitchass bitchass")
    if message.content == "November":
        await client.send_message(message.channel, "If it's only masturbation, I'm good.")
TOKEN = "NTI3NjIwODA1ODk1Mzg5MjIw.DwXrWg.qEfz6uzloclYzIoVrxlTZu87eJE"
client.run(TOKEN)