import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print("Connected!\n-----");
	print("Logged in as " + client.user.name)
	print(client.user.id);
	print("------")
	await client.change_presence(game=discord.Game(name="Nothing"))


def private_message(message):
	print("This is a private message, and will be taken very seriously")	
	
	if(len(message.attachments) > 0):
		print("Number of attachments: %s" % len(message.attachments))
		print(message.attachments[0])

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	print("Message recieved!")
	print(message.content)
		
	if message.content.lower().find("fuck you") != -1:
		await client.send_message(message.channel, "Bitchass bitchass")
	if message.content.lower().find("november") != -1:
		await client.send_message(message.channel, "If it's only masturbation, I'm good.", tts=True)
	if message.channel.is_private:
		private_message(message)
	print("-----");

		


TOKEN = "NTI3NjIwODA1ODk1Mzg5MjIw.DwXrWg.qEfz6uzloclYzIoVrxlTZu87eJE"
print("Connecting...");
client.run(TOKEN)

