import os
import discord 
import wolframalpha
import wikipedia
from keep_alive import keep_alive


tkn = os.environ['TOKEN']
app_id = os.environ['app_id']

client = discord.Client()
client2 = wolframalpha.Client(app_id)


def qna(query):

  question = query
  res = client2.query(question)
  answer = next(res.results).text
  return answer


@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event

async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$db$'):
    if len(message.content) > 4:
      query = message.content[4:]
      await message.channel.send(qna(query))
  
  if message.content.startswith('$dbwiki$'):
    if len(message.content) > 8:
      query = message.content[8:]
      answer = wikipedia.summary(query)
      answer = answer[:1910]
      await message.channel.send( "```" + answer + "......... " + "*** Please visit Wikipedia to read rest of the article ***" + "```" )
      
keep_alive()
client.run(tkn)
