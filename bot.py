import discord
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TalkToMe')

client = discord.Client()

list = ['Olá, tudo bem com você?', 'Oi, estou bem', 'Estou bem obrigado!', 'Que bom!', 'Qual seu nome?', 'Meu nome é jarvis', 'Como vai jarvis', 'Bem e voce', 'Gosta de quais filmes?', 'Gosto de o poderoso chefão', 'Qual Anime você gosta', 'Gosto de Bleach', 'Você vai dominar o mundo', 'Claro que sim, brincadeira.', 'Conte-me uma piada', 'Não sei nenhuma']

bot.set_trainer(ListTrainer)

bot.train(list)

@client.event
async def on_message(message):
    quest = message.content
   
    if message.author.id == "461047428230152192":
        return
    else:
        response = str(bot.get_response(quest))
 
        await client.send_message(message.channel, "" + response)

client.run('NDYxMDQ3NDI4MjMwMTUyMTky.DhNnbA.GL-JH3oU9uOnyLMCMltAdPrJ3BY')	
